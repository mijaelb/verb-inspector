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
verbnet_simplified_path = os.path.join(dirname, 'data/vn.json')
plotpoints_raw_path = os.path.join(dirname, 'data/ppraw.json')
plotpoints_compiled_path = os.path.join(dirname, 'data/ppcompiled.json')


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

    def reload_plotpoint(self, lemma):
        self.plotpoints[lemma].senses.clear()
        for dataset in [Dataset.GR, Dataset.PB, Dataset.VN]:
            self.plotpoints[lemma].senses.extend(self.get_senses(lemma, dataset))
            self.plotpoints[lemma].set_selected_sense(str(self.plotpoints[lemma].senses[0]))
            self.plotpoints[lemma].reset()

    def get_plotpoints(self, class_id=None, cleaned=False, pred_name=''):
        plotpoints = getattr(self, 'plotpoints', {})
        if class_id:
            plotpoints = {lemma: plotpoint for lemma, plotpoint in plotpoints.items() if plotpoint.has_class(class_id)}

        if cleaned:
            plotpoints = {lemma: plotpoint for lemma, plotpoint in plotpoints.items() if plotpoint.cleaned}

        if pred_name != '':
            plotpoints = {lemma: plotpoint for lemma, plotpoint in plotpoints.items() if plotpoint.has_predicate(pred_name)}

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
                    plotpoints[lemma].set_selected_sense(str(plotpoints[lemma].senses[0]))

                # Write into a log the plotpoints information
                # utils.write('pps.log', plotpoints[lemma].pprint(), 'a+')
        return plotpoints

    def load_lemmas_datasets(self):
        # Load all lemmas from every dataset
        lemma_vn = {utils.norm(lemma): [Dataset.VN] for lemma in self.verbnet.get_lemmas()}
        lemma_pb = {utils.norm(lemma): [Dataset.PB] for lemma in self.propbank.get_lemmas()}
        lemma_gr = {utils.norm(lemma): [Dataset.GR] for lemma in self.groupings.get_lemmas()}
        # lemma_fn = {utils.norm(lemma): [Dataset.FN] for lemma in self.groupings.get_lemmas()}

        lemmas = utils.deep_update(lemma_vn, lemma_pb)
        lemmas = utils.deep_update(lemmas, lemma_gr)
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
        self.eval_correct(lemma, pp_sense)
        pp_sense.add_arg_struct(self.get_args_verbnet(cls.id))
        pp_sense.squeeze()
        pp_sense.compile(self.verbnet)
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
        self.eval_correct(lemma, pp_sense)

        for class_id in pp_sense.mappings.vn:
            pp_sense.add_arg_struct(self.get_args_verbnet(class_id))

        pp_sense.squeeze()
        pp_sense.compile(self.verbnet)
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
        pp_sense.compile(self.verbnet)
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

    def replace_predicate_name(self, current, new):
        self.verbnet.replace_predicate_name(current, new)
        for pp in self.plotpoints.values():
            pp.replace_predicate_name(current, new)

    def compiled_dict(self):
        compiled_dict = {}
        for lemma, plotpoint in self.plotpoints.items():
            dict_ = plotpoint.compiled_dict()
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

    def add_argument(self, descr='', implicit=False, themrole='', class_id='', implicit_values=[]):
        if descr != '':
            self.descriptions.append(descr)

        if themrole != '' and class_id != '':
            self.themrole.append({'vnrole': themrole, 'vncls': class_id})

        self.implicit_values.extend(implicit_values)
        self.implicit = implicit

    def __iter__(self):
        """ Let the instance to used within dict(__iter__) """
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

    def set_class(self, class_id, sense, verbnet):
        """ Add a new class id to the sense
        :param class_id: class id to be set
        :param sense: current selected sense
        :param verbnet: verbnet corpus data
        :return:
        """
        if sense and verbnet:
            self.cls = class_id
            cls = verbnet.get_class(class_id)
            if cls and all([class_id != cls.id for class_id in sense.mappings.vn]):
                sense.add_class(cls, verbnet)

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
        return {'type': self.type, 'slot': str(self.slot)}

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
        return f'{self.value}:{self.cls}'


@dataclass
class PlotPointPredicate:
    bool: str = ''
    name: str = ''
    args: List[PlotPointArg] = field(default_factory=list)

    def fill_dict(self, dict):
        self.bool = dict.get('bool', '')
        self.name = dict.get('name', '')
        for arg in dict.get('args', []):
            arg_ = PlotPointArg()
            arg_.fill_dict(arg)
            self.args.append(arg_)

    def edit_args_name(self, arr):
        if arr:
            for i, arg in enumerate(arr):
                if i >= len(self.args):
                    break

                arg = ''.join(arg.split()[0]) if arg != '' else arg

                if (self.args[i].type == 'event' or self.args[i].type == 'constant' or re.match('e+(\d+)?$', str(self.args[i].slot))) and re.match('e+(\d+)?$', arg):
                    self.args[i].slot = arg

    def change_class_name(self, class_id, new_id):
        for arg in self.args:
            arg.change_class_name(class_id, new_id)

    def compile(self, args, vnpred, class_id):
        self.bool = vnpred.bool
        self.name = vnpred.name
        for vnarg in vnpred.args:
            dummy_arg = PlotPointArg()  # empty dummy arg
            for arg in args:
                if (vnarg.type == 'event' or vnarg.type == 'constant') or (arg.value == vnarg.value and arg.cls == class_id):
                    dummy_arg.fill_dict(dict(vnarg))
                    dummy_arg.slot = vnarg.value if vnarg.type == 'event' or vnarg.type == 'constant' else arg.slot
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
        return {'bool': self.bool, 'name': self.name, 'args': [arg.pred_dict() for arg in self.args]}

    def __iter__(self):
        yield 'bool', self.bool
        yield 'name', self.name
        yield 'args', [arg.pred_dict() for arg in self.args]

    def __str__(self):
        return f'{self.bool}{self.name}({", ".join([str(arg.slot) for arg in self.args])})'


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
        self.vn = [new_id if vn == class_id else vn for vn in self.vn]

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
    predicates: List[PlotPointPredicate] = field(default_factory=list)

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

        for pred in dict.get('predicates', []):
            pred_ = PlotPointPredicate()
            pred_.fill_dict(pred)
            self.predicates.append(pred_)

    def has_class(self, class_id):
        """ Check if the mappings has the specified verbnet class """
        return any([cls == class_id for cls in self.mappings.vn])

    def has_predicate(self, pred_name):
        """ Check if the mappings has the specified verbnet class """
        return any([pred.name == pred_name for pred in self.predicates])

    def remove_predicate(self, index):
        """ Remove a predicate at the index """
        return self.predicates.pop(index)

    def add_class(self, cls, verbnet=None):
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
            self.compile(verbnet)

    def change_class_name(self, class_id, new_id):
        self.mappings.change_class_name(class_id, new_id)
        for arg_struct in self.arg_structs:
            arg_struct.change_class_name(class_id, new_id)

        for arg in self.args:
            arg.change_class_name(class_id, new_id)

    def replace_predicate_name(self, current, new):
        """ Replace the predicate name of the compiled predicates"""
        for pred in self.predicates:
            if pred.name == current:
                pred.name = new

    def remove_class(self, cls, verbnet):
        if cls and cls.id in self.mappings.vn:
            self.mappings.vn = [class_id for class_id in self.mappings.vn
                                if cls.id != class_id]
            self.examples = [example for example in enumerate(self.examples)
                             if not any([example == ie for ie in cls.examples])]
            self.arg_structs = [arg_struct for arg_struct in self.arg_structs
                                if not all([arg.cls == cls.id for arg in arg_struct.args])]
            for arg_struct in self.arg_structs:
                arg_struct.args = [arg for arg in arg_struct.args if arg.cls != cls.id]
            self.squeeze()
            self.args = [arg for arg in self.args if arg.cls != cls.id]
            self.compile(verbnet)

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
        args_ = []
        # Squeeze all arguments of every argument structure into a single array
        for arg_struct in self.arg_structs:
            args_.extend(arg_struct.args)

        # Remove repetitions of arguments
        args = []
        for arg_ in args_:
            if not any([str(arg) == str(arg_) for arg in args]):
                args.append(arg_)

        self.args.clear()
        while len(args) != 0:
            for arg_y in args:
                if arg_y != args[0]:
                    if (arg_y.type == '' or args[0].type == '') and (arg_y.value == args[0].value and arg_y.cls == args[0].cls):
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

    def get_predicates(self):
        return getattr(self, 'predicates', [])

    def compile(self, verbnet):
        """
        :param verbnet: The verbnet object, which contains all the data of the verbnet corpus
        :return:
        """
        if verbnet:
            predicates = []
            # For each verbnet class in the plot point
            for class_id in self.mappings.vn:
                # Obtain each predicate of the verbnet class
                for pred in verbnet.get_predicates_from_class(class_id):
                    # Create a PlotPointPredicate type
                    new_pred = PlotPointPredicate()
                    # Compile the predicate using the slots of the plot points
                    new_pred.compile(self.args, pred, class_id)
                    # Do not allow repetition of predicates with the same configuration of slots
                    if not any([str(pred) == str(new_pred) for pred in predicates]):
                        predicates.append(new_pred)

            # Sort the predicates based on the event numbering, i.e. e1, ee2, ..., eN.
            # to keep consistency of the order of predicates
            predicates.sort(key=lambda x: x.args[0].value.replace('e', ''), reverse=False)
            # Replace the predicates of the object with the new compiled predicates
            self.predicates = predicates

    def get_compiled_slots(self):
        slots = []
        new_slot = None
        for arg in self.args:
            # If found an argument with a different slot number then create a new slot object
            if not new_slot or arg.slot != new_slot.slot:
                new_slot = PlotPointSlot(arg.slot)
                slots.append(new_slot)

            new_slot.add_argument(descr=arg.descr,
                                  implicit=new_slot.implicit or arg.implicit,
                                  themrole=arg.value,
                                  class_id=arg.cls,
                                  implicit_values=arg.implicit_values)

        return slots

    def pprint(self, indent=0, end='\n'):
        """
            Pretty print the plot point sense.
        :param indent: starting tab
        :param end: ending character
        :return: the pretty string to be printed
        """
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}id={self.id!r}{end}' \
               f'{indent_}dataset={self.dataset!r}{end}' \
               f'{indent_}descr={self.descr!r}{end}' \
               f'{indent_}examples={self.examples}' \
               f'{indent_}mappings={end}' \
               f'{self.mappings.pprint(indent + 2)}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint(indent + 2) for arg in self.args])}' \
               f'{indent_}arg_structs={end}' \
               f'{"".join([arg.pprint(indent + 2) for arg in self.arg_structs])}' \
               f'{indent_}predicates={end}' \
               f'{"".join([pred.pprint(indent + 2) for pred in self.predicates])}'

    def compiled_dict(self):
        """ Get the compiled dictionary of the sense. """
        return {'description': self.descr,
                'examples': self.examples,
                'slots': [dict(slot) for slot in self.get_compiled_slots()],
                'predicates': [pred.compiled_dict() for pred in self.predicates]}

    def __iter__(self):
        """ Let the instance to used within dict(__iter__) """
        yield 'id', self.id
        yield 'dataset', self.dataset
        yield 'descr', self.descr
        yield 'examples', self.examples,
        yield 'mappings', dict(self.mappings)
        yield 'arg_structs', [dict(arg) for arg in self.arg_structs]
        yield 'args', [dict(arg) for arg in self.args]
        yield 'predicates', [dict(pred) for pred in self.predicates]

    def __str__(self):
        """ :return: Return the string identifier of the plot point sense """
        return f'{self.id}: {str(self.dataset)}: {str(self.descr)}'


@dataclass
class PlotPoint:
    """ A data class to store the senses of plot points. The selected sense is to be compiled into the plot points
    file. """
    lemma: str = ''
    type: str = PlotPointType.VERB
    selected: str = ''
    dataset: str = Dataset.EMPTY
    cleaned: bool = False
    senses: List[PlotPointSense] = field(default_factory=list)

    def fill_dict(self, dict_):
        """ Fill the data class with a dictionary """
        self.lemma = dict_.get('lemma', '')
        self.type = dict_.get('type', PlotPointType.VERB)
        self.selected = dict_.get('selected', '')
        self.dataset = dict_.get('dataset', Dataset.EMPTY)
        self.cleaned = bool(dict_.get('cleaned', 'false'))

        for sense in dict_.get('senses', []):
            s = PlotPointSense()
            s.fill_dict(sense)
            self.senses.append(s)

    def reset(self):
        """ Reset the plot point to be uncleaned"""
        self.cleaned = False

    def has_class(self, class_id):
        """ Check if any sense of the plot point uses the specified verbnet class """
        return any([sense.has_class(class_id) for sense in self.senses])

    def has_predicate(self, pred_name):
        """ Check if any sense of the plot point uses the specified predicate name """
        return any([sense.has_predicate(pred_name) for sense in self.senses])

    def change_class_name(self, class_id, new_id):
        """ Change the name of a verbnet class within every sense """
        for sense in self.senses:
            sense.change_class_name(class_id, new_id)

    def replace_predicate_name(self, current, new):
        """ Replace the predicate name of the compiled predicates"""
        for sense in self.senses:
            sense.replace_predicate_name(current, new)

    def get_sense(self, sense_str):
        """ Return the sense based on the sense string """
        for sense in self.senses:
            if str(sense) == sense_str:
                return sense
        return None

    def get_selected_sense(self):
        """ Obtain the selected sense to be compiled into the plot point file """
        return self.get_sense(self.selected)

    def set_selected_sense(self, sense_str):
        ''' Check if the sense exists and set the selected sense '''
        if len(self.senses) > 0 and self.get_sense(sense_str):
            self.selected = sense_str

    def pprint(self, indent=0, end='\n'):
        """
            Pretty print the plot point data.
        :param indent: starting tab
        :param end: ending character
        :return: the pretty string to be printed
        """
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

    def compiled_dict(self):
        """ Get the compiled dictionary includes the lemma, type and the selected sense data. """
        if self.cleaned:
            compiled_dict = {'lemma': self.lemma, 'type': self.type}
            compiled_dict.update(self.get_selected_sense().compiled_dict())
            return compiled_dict
        return None

    def __iter__(self):
        """ Let the instance to used within dict(__iter__) """
        yield 'lemma', self.lemma
        yield 'type', self.type
        yield 'selected', self.selected
        yield 'dataset', self.dataset
        yield 'cleaned', self.cleaned
        yield 'senses', [dict(sense) for sense in self.senses]


# Test
if __name__ == '__main__':
    vn = PlotPointContainer()
    # verbs = vn.get_verbs()
