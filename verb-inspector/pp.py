import bs4
import re
import json
import os
import sys
from pathlib import Path
from itertools import chain
from collections import Counter
from utils import utils
from dataclasses import field, dataclass
from typing import List
import gr
import pb
import vn
from enum import Enum


class Dataset:
    VN = 'vn'
    PB = 'pb'
    GR = 'gr'
    FN = 'fn'
    PP = 'pp'
    EMPTY = ''


class PlotPointType:
    VERB = 'verb'
    PREP = 'prep'
    EMPTY = ''


dirname = os.path.dirname(__file__)
groupings_path = os.path.join(dirname, 'corpora/ontonotes/sense-inventories/')
propbank_path = os.path.join(dirname, 'corpora/propbank/frames/')
verbnet_path = os.path.join(dirname, 'corpora/verbnet/')
vnpb_path = os.path.join(dirname, 'corpora/mappings/vnpb-mappings.json')
verbnet_simplified_path = os.path.join(dirname, 'data/verbnet.json')
plotpoints_raw_path = os.path.join(dirname, 'data/plotpoints_raw.json')
plotpoints_compiled_path = os.path.join(dirname, 'data/plotpoints_compiled.json')


class PlotPointContainer(object):
    def __init__(self):
        self.json_path = plotpoints_raw_path
        self.json = utils.fromjson(self.json_path)

        # self.vnpb = utils.fromjson(vnpb_path)
        self.verbnet = vn.VerbNetSimplified(verbnet_path, verbnet_simplified_path)
        self.propbank = pb.PropBank(propbank_path)
        self.groupings = gr.Groupings(groupings_path)

        self.bso = ''
        self.plotpoints = self.load_plotpoints()

    def load(self, filename=''):
        if filename:
            json_path = filename
            json = utils.fromjson(filename)
        elif self.json_path:
            json_path = self.json_path
            json = utils.fromjson(self.json_path)

        if json:
            self.json_path = json_path
            self.json = json
            self.plotpoints = self.load_plotpoints()

    def save(self, filename=''):
        if filename:
            utils.tojson(filename, dict(self))
        elif self.json_path:
            utils.tojson(self.json_path, dict(self))

    def compile(self, filename):
        if filename:
            utils.tojson(filename, self.compiled_dict())

    def get_plotpoints(self, class_id=None):
        plotpoints = getattr(self, 'plotpoints', {})
        if class_id:
            plotpoints = {lemma: plotpoint for lemma, plotpoint in plotpoints.items() if plotpoint.has_class(class_id)}

        return plotpoints

    def load_plotpoints(self):
        plotpoints = {}
        if self.json:
            for lemma, plotpoint in self.json.items():
                plotpoints[lemma] = PlotPoint()
                plotpoints[lemma].fill_dict(plotpoint)
        else:
            lemmas = self.load_lemmas_datasets()
            for lemma, datasets in lemmas.items():
                plotpoints[lemma] = PlotPoint(lemma, PlotPointType.VERB)
                for dataset in datasets:
                    plotpoints[lemma].senses.extend(self.get_senses(lemma, dataset))

                # Set selected sense by default the first in the list
                if len(plotpoints[lemma].senses) > 0:
                    plotpoints[lemma].selected = plotpoints[lemma].senses[0]

                # Write into a log the plotpoints information
                # utils.write('pps.log', plotpoints[lemma].pprint(), 'a+')
        return plotpoints

    def load_lemmas_datasets(self):
        # Load all lemmas from every dataset
        lemmas = {utils.norm(lemma): [Dataset.VN] for lemma in self.verbnet.get_lemmas()}
        lemmas = utils.deep_update(lemmas,
                                   {utils.norm(lemma): [Dataset.PB] for lemma in self.propbank.get_lemmas()})
        lemmas = utils.deep_update(lemmas,
                                   {utils.norm(lemma): [Dataset.GR] for lemma in self.groupings.get_lemmas()})
        # lemmas = utils.deep_update(lemmas, {utils.norm(lemma): [Dataset.FN] for lemma in self.groupings.get_lemmas()})
        lemmas = dict(sorted(lemmas.items(), key=lambda x: x[0].lower()))

        return lemmas

    def get_senses(self, lemma, dataset):
        pp_senses = []
        if dataset == Dataset.GR:
            found = False
            for sense in self.groupings.get_senses(lemma).values():
                found = True
                pp_senses.append(self.get_sense_grouping(lemma, sense))
            if not found: print(lemma + ' ' + Dataset.GR)
        elif dataset == Dataset.PB:
            found = False
            for roleset in self.propbank.get_rolesets(lemma):
                found = True
                pp_senses.append(self.get_sense_propbank(lemma, roleset))
            if not found: print(lemma + ' ' + Dataset.PB)
        elif dataset == Dataset.VN:
            found = False
            for cls in self.verbnet.get_classes(lemma).values():
                found = True
                pp_senses.append(self.get_class_verbnet(lemma, cls))
            if not found: print(lemma + ' ' + Dataset.VN)
        return pp_senses

    def get_class_verbnet(self, lemma, cls):
        pp_sense = PlotPointSense(cls.id, Dataset.VN, '')
        pp_sense.mappings.wn = cls.get_member(lemma).get_wn()
        pp_sense.mappings.vn = [cls.id]
        pp_sense.mappings.pb = self.propbank.get_rolesets_ids_from_class(lemma, cls.id)
        pp_sense.mappings.gr = cls.get_member(lemma).get_gr()
        pp_sense.mappings.fn = [fn.lower() for fn in cls.get_member(lemma).get_fn()]
        pp_sense.add_examples(cls.get_examples())
        self.eval_correct(lemma, pp_sense.mappings)
        pp_sense.add_arg_struct(self.get_args_verbnet(cls.id))
        pp_sense.squeeze()
        return pp_sense

    def get_sense_propbank(self, lemma, roleset):
        pp_sense = PlotPointSense(roleset.id, Dataset.PB, roleset.name)
        pp_sense.mappings.wn = []
        pp_sense.mappings.vn = self.verbnet.get_complete_classes_ids(roleset.get_classes())
        pp_sense.mappings.pb = [roleset.id]
        pp_sense.mappings.gr = self.groupings.get_senses_ids_from_propbank(lemma, roleset.id)
        pp_sense.mappings.fn = list(
            dict.fromkeys([fn.lower()
                           for fn in
                           (self.verbnet.get_fn_from_classes(lemma, pp_sense.mappings.vn) + roleset.get_fn())]))
        pp_sense.add_examples(roleset.get_examples_text())
        pp_sense.add_arg_struct(self.get_args_propbank(roleset.id))
        self.eval_correct(lemma, pp_sense.mappings)

        for class_id in pp_sense.mappings.vn:
            pp_sense.add_arg_struct(self.get_args_verbnet(class_id))

        pp_sense.squeeze()
        return pp_sense

    def get_sense_grouping(self, lemma, sense):
        pp_sense = PlotPointSense(sense.id, Dataset.GR, sense.name)
        pp_sense.mappings.wn = sense.mappings.wn

        gr_vn = self.verbnet.get_classes_ids_from_grouping(lemma, sense.id)
        for roleset in sense.mappings.pb:
            gr_vn.extend(self.verbnet.get_complete_classes_ids(self.propbank.get_classes(roleset)))

        pp_sense.mappings.vn = list(dict.fromkeys([vn.lower() for vn in (sense.mappings.vn + gr_vn)]))
        pp_sense.mappings.pb = sense.mappings.pb
        pp_sense.mappings.gr = [sense.id]
        pp_sense.mappings.fn = list(dict.fromkeys([fn.lower()
                                                   for fn in (self.verbnet.get_fn_from_classes(lemma,
                                                                                               pp_sense.mappings.vn) + sense.mappings.fn)]))
        pp_sense.add_examples(sense.examples)
        self.eval_correct(lemma, pp_sense)

        for roleset in pp_sense.mappings.pb:
            pp_sense.add_arg_struct(self.get_args_propbank(roleset))

        for class_id in pp_sense.mappings.vn:
            pp_sense.add_arg_struct(self.get_args_verbnet(class_id))

        pp_sense.squeeze()
        return pp_sense

    def eval_correct(self, lemma, pp_sense):
        for vn in pp_sense.mappings.vn:
            cls = self.verbnet.get_class(vn)
            if not cls:
                utils.write('eval.log', f'{lemma} VN: {vn}\n', 'a+')

        for gr in pp_sense.mappings.gr:
            sense = self.groupings.get_sense(gr)
            if not sense:
                utils.write('eval.log', f'{lemma} GR: {gr}\n', 'a+')

        for i, pb in enumerate(pp_sense.mappings.pb):
            roleset = self.propbank.get_roleset(pb)
            if not roleset:
                utils.write('eval.log', f'{lemma} PB: {pb} Corrected: {self.propbank.get_corrected_roleset_name(pb)}\n',
                            'a+')
                pb_ = self.propbank.get_corrected_roleset_name(pb)
                pp_sense.mappings.pb[i] = pb_ if pb_ else pb

        # TODO: Connect FrameNet

    def get_args_propbank(self, roleset):
        roles = self.propbank.get_roles(roleset)
        return self.transform_roles(roles, roleset, Dataset.PB) if roles else None

    def get_args_verbnet(self, class_id):
        cls = self.verbnet.get_class(class_id)
        return self.transform_roles(cls.get_args(), class_id, Dataset.VN) if cls else None

    def transform_roles(self, roles, id, dataset):
        if dataset == Dataset.PB:
            arg_struct = PlotPointArgStruct(id, dataset)
            for role in roles:
                slot = int(role.n) if role.n.isdigit() else len(arg_struct.args) - 1
                if role.vnroles:
                    for vnrole in role.vnroles:
                        id = self.verbnet.get_complete_class_id(vnrole.vncls)
                        arg_struct.add_arg(PlotPointArg(role.descr, role.f, vnrole.vntheta,
                                                        id, slot, False, dataset))
                else:
                    arg_struct.add_arg(PlotPointArg(role.descr, role.f, '', '', slot, False, dataset))
        elif dataset == Dataset.VN:
            id = self.verbnet.get_complete_class_id(id)
            arg_struct = PlotPointArgStruct(id, dataset)
            for i, role in enumerate(roles):
                arg_struct.add_arg(PlotPointArg('', '', role.value, id, int(role.slot), role.implicit, dataset))

        return arg_struct

    def change_class_name(self, class_id, new_id):
        if self.verbnet.change_class_name(class_id, new_id):
            for pp in self.plotpoints.values():
                pp.change_class_name(class_id, new_id)

    def compiled_dict(self):
        compiled_dict = {}
        for lemma, plotpoint in self.plotpoints.items():
            dict_ = plotpoint.compiled_dict(self.verbnet)
            if dict_:
                compiled_dict[lemma] = dict_
        return compiled_dict

    def __iter__(self):
        for lemma, plotpoint in self.plotpoints.items():
            yield lemma, dict(plotpoint)


@dataclass
class PlotPointSlot:
    slot: int = -1
    descriptions: list = field(default_factory=list)
    themrole: list = field(default_factory=list)
    implicit: bool = False
    implicit_values: list = field(default_factory=list)

    def add_descr(self, descr):
        if descr != '':
            self.descriptions.append(descr)

    def add_themrole(self, role, class_id):
        if role != '' and class_id != '':
            self.themrole.append({'vnrole': role, 'vncls': class_id})

    def add_implicit_values(self, values):
        self.implicit_values.extend(values)

    def __iter__(self):
        yield 'slot', self.slot
        yield 'descriptions', self.descriptions
        yield 'themrole', self.themrole
        yield 'implicit', self.implicit
        yield 'implicit_values', self.implicit_values


@dataclass
class PlotPointArg:
    descr: str = ''
    type: str = ''
    value: str = ''
    cls: str = ''
    slot: int = -1
    implicit: bool = False
    dataset: str = Dataset.EMPTY
    implicit_values: list = field(default_factory=list)

    def fill_dict(self, dict):
        self.descr = dict.get('descr', '')
        self.type = dict.get('type', '')
        self.value = dict.get('value', '')
        self.cls = dict.get('cls', '')
        self.slot = dict.get('slot', -1)
        self.implicit = bool(dict.get('implicit', 'false'))
        self.dataset = dict.get('dataset', Dataset.EMPTY)
        self.implicit_values = dict.get('implicit_values', list())

    def set_class(self, class_id, sense=None, verbnet=None):
        if sense:
            self.cls = class_id
            cls = verbnet.get_class(class_id)
            if not verbnet or cls:
                if all([class_id != cls.id for class_id in sense.mappings.vn]):
                    sense.add_class(cls)

    def change_class_name(self, class_id, new_id):
        self.cls = new_id if self.cls == class_id else self.cls

    def combine(self, arg):
        self.descr = arg.descr if self.descr == '' else self.descr
        self.type = arg.type if self.type == '' else self.type
        self.value = arg.value if self.value == '' else self.value
        self.cls = arg.cls if self.cls == '' else self.cls
        self.slot = arg.slot if self.slot == -1 else self.slot
        self.implicit = arg.implicit if not self.implicit else self.implicit
        self.dataset = Dataset.PP
        self.implicit_values = arg.implicit_values if not self.implicit_values else self.implicit_values

    def pred_dict(self):
        return {'type': self.type, 'slot': str(self.slot) if self.slot != -1 else
        (self.value if self.type == 'event' else 'nan')}

    def pprint(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}descr={self.descr}{end}' \
               f'{indent_}type={self.type}{end}' \
               f'{indent_}value={self.value}{end}' \
               f'{indent_}cls={self.cls}{end}' \
               f'{indent_}slot={self.slot}{end}' \
               f'{indent_}implicit={self.implicit}{end}' \
               f'{indent_}implicit_values={self.implicit_values}{end}' \
               f'{indent_}dataset={self.dataset}{end}'

    def pprint_pred(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}type={self.type}{end}' \
               f'{indent_}value={self.cls}{end}'

    def __iter__(self):
        yield 'descr', self.descr
        yield 'type', self.type
        yield 'value', self.value
        yield 'cls', self.cls
        yield 'slot', self.slot
        yield 'implicit', self.implicit
        yield 'implicit_values', self.implicit_values
        yield 'dataset', self.dataset

    def __str__(self):
        return self.value if self.type == 'event' else str(self.slot)


@dataclass
class PlotPointPredicate:
    bool: str = ''
    name: str = ''
    args: List[PlotPointArg] = field(default_factory=list)

    def change_class_name(self, class_id, new_id):
        for arg in self.args:
            arg.change_class_name(class_id, new_id)

    def compile(self, args, vnpred, class_id):
        self.bool = vnpred.bool
        self.name = vnpred.name
        for vnarg in vnpred.args:
            dummy_arg = PlotPointArg()  # empty dummy predicate
            for arg in args:
                if vnarg.type == 'event':
                    dummy_arg.fill_dict(dict(vnarg))
                    break
                elif arg.value == vnarg.value and arg.cls == class_id:
                    dummy_arg.fill_dict(dict(vnarg))
                    dummy_arg.slot = arg.slot
                    break
            self.args.append(dummy_arg)

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}bool={self.bool!r}{end}' \
               f'{indent_}name={self.name!r}{end}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint_pred(indent + 2, end) for arg in self.args])}'

    def compiled_dict(self):
        return {'bool': self.bool,
                'name': self.name,
                'args': [arg.pred_dict() for arg in self.args]}

    def __iter__(self):
        yield 'bool', self.bool
        yield 'name', self.name
        yield 'args', [arg.pred_dict() for arg in self.args]

    def __str__(self):
        return f'{self.bool}{self.name}({", ".join([str(arg) for arg in self.args])})'


@dataclass
class PlotPointArgStruct:
    id: str = ''
    dataset: str = Dataset.EMPTY
    args: List[PlotPointArg] = field(default_factory=list)

    def fill_dict(self, dict):
        self.id = dict.get('id', '')
        self.dataset = dict.get('dataset', '')
        for arg in dict.get('args', []):
            arg_ = PlotPointArg()
            arg_.fill_dict(arg)
            self.args.append(arg_)

    def add_arg(self, pp_arg):
        self.args.append(pp_arg)

    def change_class_name(self, class_id, new_id):
        for arg in self.args:
            arg.change_class_name(class_id, new_id)

    def pprint(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}id={self.id}{end}' \
               f'{indent_}dataset={self.dataset}{end}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint(indent + 2) for arg in self.args])}'

    def __iter__(self):
        yield 'id', self.id
        yield 'dataset', self.dataset
        yield 'args', [dict(arg) for arg in self.args]


@dataclass
class PlotPointMapping:
    wn: list = field(default_factory=list)
    vn: list = field(default_factory=list)
    fn: list = field(default_factory=list)
    gr: list = field(default_factory=list)
    pb: list = field(default_factory=list)

    def fill_dict(self, dict):
        self.wn = dict.get('wn', [])
        self.vn = dict.get('vn', [])
        self.fn = dict.get('fn', [])
        self.gr = dict.get('gr', [])
        self.pb = dict.get('pb', [])

    def change_class_name(self, class_id, new_id):
        for i, vn in enumerate(self.vn):
            if vn == class_id:
                self.vn[i] = new_id

    def pprint(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}wn={self.wn!r}{end}' \
               f'{indent_}vn={self.vn!r}{end}' \
               f'{indent_}fn={self.fn!r}{end}' \
               f'{indent_}gr={self.gr!r}{end}' \
               f'{indent_}pb={self.pb!r}{end}'

    def __iter__(self):
        yield 'wn', self.wn
        yield 'vn', self.vn
        yield 'fn', self.fn
        yield 'gr', self.gr
        yield 'pb', self.pb


@dataclass
class PlotPointSense:
    id: str = ''
    dataset: str = Dataset.EMPTY
    descr: str = ''
    mappings: PlotPointMapping = field(default_factory=PlotPointMapping)
    examples: list = field(default_factory=list)
    arg_structs: List[PlotPointArgStruct] = field(default_factory=list)
    args: List[PlotPointArg] = field(default_factory=list)

    def fill_dict(self, dict):
        self.id = dict.get('id', '')
        self.dataset = dict.get('dataset', Dataset.EMPTY)
        self.descr = dict.get('descr', '')
        self.mappings = PlotPointMapping()
        self.mappings.fill_dict(dict.get('mappings', {}))
        self.examples = dict.get('examples', [])
        for arg_struct in dict.get('arg_structs', []):
            struct = PlotPointArgStruct()
            struct.fill_dict(arg_struct)
            self.arg_structs.append(struct)

        for arg in dict.get('args', []):
            arg_ = PlotPointArg()
            arg_.fill_dict(arg)
            self.args.append(arg_)

    def has_class(self, class_id):
        for cls in self.mappings.vn:
            if cls == class_id:
                return True

        return False

    def add_class(self, cls):
        if cls and cls.id not in self.mappings.vn:
            self.mappings.vn.append(cls.id)
            for example in cls.examples:
                if not any([example == ie for ie in self.examples]):
                    self.examples.append(example)

            arg_struct = PlotPointArgStruct(cls.id, Dataset.VN)
            for i, arg in enumerate(cls.args):
                arg_struct.add_arg(PlotPointArg('', '', arg.value, cls.id, int(arg.slot), arg.implicit, Dataset.VN))

            self.arg_structs.append(arg_struct)
            self.squeeze()

    def change_class_name(self, class_id, new_id):
        self.mappings.change_class_name(class_id, new_id)
        for arg_struct in self.arg_structs:
            arg_struct.change_class_name(class_id, new_id)

        for arg in self.args:
            arg.change_class_name(class_id, new_id)

    def remove_class(self, cls):
        if cls and cls.id in self.mappings.vn:
            self.mappings.vn = [class_id for class_id in self.mappings.vn if cls.id != class_id]
            self.examples = [example for example in enumerate(self.examples) if
                             not any([example == ie for ie in cls.examples])]
            self.arg_structs = [arg_struct for arg_struct in self.arg_structs if
                                not all([arg.cls == cls.id for arg in arg_struct.args])]
            for arg_struct in self.arg_structs:
                arg_struct.args = [arg for arg in arg_struct.args if arg.cls != cls.id]
            self.squeeze()
            self.args = [arg for arg in self.args if arg.cls != cls.id]
            print(str(self.args))

    def add_arg_struct(self, arg_struct):
        if arg_struct:
            self.arg_structs.append(arg_struct)

    def add_arg(self, value='empty', cls='', slot=0, implicit=False):
        i = -1
        for i, arg in enumerate(self.args):
            if arg.slot > slot:
                break
        self.args.insert(i + 1, PlotPointArg('', '', value, cls, slot, implicit, Dataset.PP))

    def get_args(self):
        return self.args

    def squeeze(self):
        args = []
        for arg_struct in self.arg_structs:
            args.extend(arg_struct.args)

        self.args.clear()
        while len(args) != 0:
            for arg_y in args:
                if arg_y != args[0]:
                    if (arg_y.type == '' or args[0].type == '') and (
                            arg_y.value == args[0].value and arg_y.cls == args[0].cls):
                        args[0].combine(arg_y)
                        args.remove(arg_y)

            self.args.append(args[0])
            args.pop(0)

        self.args.sort(key=lambda x: str(x.slot), reverse=False)
        self.reorder_slots()

    def update_slots(self):
        self.__update_slots()
        self.reorder_slots()

    def __update_slots(self):
        i, j = (-1, 0)
        while j < len(self.args):
            if i != -1:
                if self.args[i].slot > self.args[j].slot:
                    self.args[i], self.args[j] = self.args[j], self.args[i]
                    self.update_slots()

            i, j = (j, j + 1)

    def reorder_slots(self):
        prev_slot = 0
        for arg in self.args:
            if arg.slot - prev_slot > 1:
                arg.slot = prev_slot + 1
            prev_slot = arg.slot

    def remove_arg(self, arg):
        for i, arg_ in enumerate(self.args):
            if arg == arg_:
                return self.args.pop(i)

    def add_examples(self, examples):
        self.examples.extend(examples)

    def get_compiled_predicates(self, verbnet):
        compiled_preds = []
        for class_id in self.mappings.vn:
            for pred in verbnet.get_predicates_from_class(class_id):
                new_pred = PlotPointPredicate()
                new_pred.compile(self.args, pred, class_id)
                compiled_preds.append(new_pred)
        return compiled_preds

    def get_compiled_slots(self):
        slots = []
        new_slot = PlotPointSlot(-10)
        for arg in self.args:
            if arg.slot != new_slot.slot:
                new_slot = PlotPointSlot(arg.slot)

            new_slot.add_descr(arg.descr)
            new_slot.implicit = new_slot.implicit or arg.implicit
            new_slot.add_themrole(arg.value, arg.cls)
            new_slot.add_implicit_values(arg.implicit_values)
            slots.append(new_slot)
        return slots

    def pprint(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}id={self.id!r}{end}' \
               f'{indent_}dataset={self.dataset!r}{end}' \
               f'{indent_}descr={self.descr!r}{end}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint(indent + 2) for arg in self.args])}' \
               f'{indent_}arg_structs={end}' \
               f'{"".join([arg.pprint(indent + 2) for arg in self.arg_structs])}' \
               f'{indent_}mappings={end}' \
               f'{self.mappings.pprint(indent + 2)}' \
               f'{indent_}examples={end}' \
               f'{self.examples.pprint(indent + 2)}'

    def compiled_dict(self, verbnet):
        return {'description': self.descr,
                'examples': list(self.examples),
                'slots': [dict(slot) for slot in self.get_compiled_slots()],
                'predicates': [pred.compiled_dict() for pred in self.get_compiled_predicates(verbnet)]}

    def __iter__(self):
        yield 'id', self.id
        yield 'dataset', self.dataset
        yield 'descr', self.descr
        yield 'mappings', dict(self.mappings)
        yield 'examples', list(self.examples),
        yield 'arg_structs', [dict(arg) for arg in self.arg_structs]
        yield 'args', [dict(arg) for arg in self.args]

    def __str__(self):
        return f'{self.id}: {str(self.dataset)}: {str(self.descr)}'


@dataclass
class PlotPoint:
    ''' A data class that stores the senses of plot points and selects the sense '''
    lemma: str = ''
    type: str = PlotPointType.VERB
    selected: PlotPointSense = None
    dataset: str = Dataset.EMPTY
    cleaned: bool = False
    senses: List[PlotPointSense] = field(default_factory=list)

    def fill_dict(self, dict):
        self.lemma = dict.get('lemma', '')
        self.type = dict.get('type', PlotPointType.VERB)
        self.dataset = dict.get('dataset', Dataset.EMPTY)
        self.cleaned = bool(dict.get('cleaned', 'false'))

        for sense in dict.get('senses', []):
            s = PlotPointSense()
            s.fill_dict(sense)
            self.senses.append(s)

        sense = dict.get('selected', None)
        sense = None if sense == '' else sense
        if sense:
            selected = PlotPointSense()
            selected.fill_dict(sense)
            for sense in self.senses:
                if str(sense) == str(selected):
                    self.selected = sense
                    break

    def has_class(self, class_id):
        return any([sense.has_class(class_id) for sense in self.senses])

    def change_class_name(self, class_id, new_id):
        for sense in self.senses:
            sense.change_class_name(class_id, new_id)

    def pprint(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}lemma={self.lemma!r}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}selected={self.selected!r}{end}' \
               f'{indent_}dataset={self.dataset!r}{end}' \
               f'{indent_}cleaned={str(self.cleaned)!r}{end}' \
               f'{indent_}senses={end}' \
               f'{"".join([sense.pprint(indent + 1) for sense in self.senses])}'

    def compiled_dict(self, verbnet):
        if self.cleaned:
            d = {'lemma': self.lemma, 'type': self.type}
            d.update(self.selected.compiled_dict(verbnet))
            return d
        return None

    def __iter__(self):
        yield 'lemma', self.lemma
        yield 'type', self.type
        yield 'selected', dict(self.selected) if self.selected else ''
        yield 'dataset', self.dataset
        yield 'cleaned', self.cleaned
        yield 'senses', [dict(sense) for sense in self.senses]


if __name__ == '__main__':
    vn = PlotPointContainer()
    # verbs = vn.get_verbs()
