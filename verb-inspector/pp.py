from enum import Enum

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


# import spacy


class Dataset(Enum):
    VN = 'vn'
    PB = 'pb'
    GR = 'gr'
    FN = 'fn'
    PP = 'pp'
    EMPTY = ''


class PlotPointType(Enum):
    VERB = 'verb'
    PREP = 'prep'
    EMPTY = ''


dirname = os.path.dirname(__file__)
groupings_path = os.path.join(dirname, 'corpora/ontonotes/sense-inventories/')
propbank_path = os.path.join(dirname, 'corpora/propbank/frames/')
verbnet_path = os.path.join(dirname, 'corpora/verbnet/')
vnpb_path = os.path.join(dirname, 'corpora/mappings/vnpb-mappings.json')
verbnet_simplified_path = os.path.join(dirname, 'data/verbnet.json')


class PlotPointContainer(object):
    def __init__(self, json_path=''):
        self.json_path = json_path
        self.verbnet = vn.VerbNetSimplified(verbnet_path, verbnet_simplified_path)

        # self.vnpb = utils.fromjson(vnpb_path)
        # self.propbank = pb.PropBank(propbank_path)
        # self.groupings = gr.Groupings(groupings_path)

        self.bso = ''
        # self.plotpoints = self.load_plotpoints()

    def get_plotpoints(self):
        return getattr(self, 'plotpoints', {})

    def load_plotpoints(self):
        plotpoints = getattr(self, 'plotpoints', {})
        if not plotpoints:
            if self.json_path:
                ...
                # pps_dict = utils.fromjson(self.json_path)
            else:
                # Load all lemmas from every dataset
                lemmas = {utils.norm(lemma): [Dataset.VN] for lemma in self.verbnet.get_lemmas()}
                lemmas = utils.deep_update(lemmas,
                                           {utils.norm(lemma): [Dataset.PB] for lemma in self.propbank.get_lemmas()})
                lemmas = utils.deep_update(lemmas,
                                           {utils.norm(lemma): [Dataset.GR] for lemma in self.groupings.get_lemmas()})
                # lemmas = utils.deep_update(lemmas, {utils.norm(lemma): [Dataset.FN] for lemma in self.groupings.get_lemmas()})
                lemmas = dict(sorted(lemmas.items(), key=lambda x: x[0].lower()))
                for lemma, datasets in lemmas.items():
                    plotpoints[lemma] = PlotPoint(lemma, PlotPointType.VERB)
                    if Dataset.GR in datasets:
                        senses = self.groupings.get_senses(lemma)
                        for sense in senses.values():
                            pp_sense = self.get_sense_grouping(lemma, sense)
                            plotpoints[lemma].add_sense(pp_sense)

                    if Dataset.PB in datasets:
                        rolesets = self.propbank.get_rolesets(lemma)
                        for roleset in rolesets:
                            pp_sense = self.get_sense_propbank(lemma, roleset)
                            plotpoints[lemma].add_sense(pp_sense)

                    if Dataset.VN in datasets:
                        classes = self.verbnet.get_classes(lemma)
                        for cls in classes.values():
                            pp_class = self.get_class_verbnet(cls, lemma)
                            plotpoints[lemma].add_sense(pp_class)

                    # Set selected sense by default the first in the list
                    if len(plotpoints[lemma].senses) > 0:
                        plotpoints[lemma].selected = plotpoints[lemma].senses[0]

                    # Write a log about it
                    # utils.write('pps.log', plotpoints[lemma].pprint(), 'a+')
        return plotpoints

    def get_class_verbnet(self, cls, lemma):
        pp_sense = PlotPointSense(cls.id, Dataset.VN, '')
        pp_sense.mappings.wn = cls.get_member(lemma).wn
        pp_sense.mappings.vn = [cls.id]
        pp_sense.mappings.pb = self.propbank.get_rolesets_ids_from_class(lemma, cls.id)
        pp_sense.mappings.gr = cls.get_member(lemma).get_gr()
        pp_sense.mappings.fn = cls.get_member(lemma).get_fn()
        pp_sense.examples.vn = cls.get_examples()

        arg_struct = self.get_args_verbnet(cls.id)
        if arg_struct:
            pp_sense.add_arg_struct(arg_struct)

        pp_sense.squeeze()
        return pp_sense

    def get_sense_propbank(self, lemma, roleset):
        pp_sense = PlotPointSense(roleset.id, Dataset.PB, roleset.name)
        pp_sense.mappings.wn = []
        pp_sense.mappings.vn = self.verbnet.get_complete_classes_ids(roleset.get_classes())
        pp_sense.mappings.pb = [roleset.id]
        pp_sense.mappings.gr = self.groupings.get_senses_ids_from_propbank(lemma, roleset.id)
        pp_sense.mappings.fn = list(dict.fromkeys(self.verbnet.get_fn_from_classes(lemma, pp_sense.mappings.vn) + roleset.get_fn()))
        pp_sense.examples.pb = roleset.get_examples_text()

        arg_struct = self.get_args_propbank(roleset.id)
        if arg_struct:
            pp_sense.add_arg_struct(arg_struct)

        for class_id in pp_sense.mappings.vn:
            arg_struct = self.get_args_verbnet(class_id)
            if arg_struct:
                pp_sense.add_arg_struct(arg_struct)

        pp_sense.squeeze()
        return pp_sense

    def get_sense_grouping(self, lemma, sense):
        pp_sense = PlotPointSense(sense.id, Dataset.GR, sense.name)
        pp_sense.mappings.wn = sense.mappings.wn

        gr_vn = self.verbnet.get_classes_ids_from_grouping(lemma, sense.id)
        for roleset in sense.mappings.pb:
            gr_vn.extend(self.verbnet.get_complete_classes_ids(self.propbank.get_classes(roleset)))

        pp_sense.mappings.vn = list(dict.fromkeys(sense.mappings.vn + gr_vn))
        pp_sense.mappings.pb = sense.mappings.pb
        pp_sense.mappings.gr = [sense.id]
        pp_sense.mappings.fn = self.verbnet.get_fn_from_classes(lemma, pp_sense.mappings.vn) + sense.mappings.fn
        pp_sense.examples.gr = sense.examples

        for roleset in pp_sense.mappings.pb:
            arg_struct = self.get_args_propbank(roleset)
            if arg_struct:
                pp_sense.add_arg_struct(arg_struct)

        for class_id in pp_sense.mappings.vn:
            arg_struct = self.get_args_verbnet(class_id)
            if arg_struct:
                pp_sense.add_arg_struct(arg_struct)

        pp_sense.squeeze()
        return pp_sense

    def get_args_propbank(self, roleset):
        roles = self.propbank.get_roles(roleset)
        if roles:
            arg_struct = self.transform_roles(roles, roleset, Dataset.PB)
            return arg_struct
        return None

    def get_args_verbnet(self, class_id):
        cls = self.verbnet.get_class(class_id)
        if cls:
            args = cls.get_args()
            arg_struct = self.transform_roles(args, class_id, Dataset.VN)
            return arg_struct
        return None

    def transform_roles(self, roles, id, dataset):
        if dataset == Dataset.PB:
            arg_struct = PlotPointArgStruct(id, dataset)
            for role in roles:
                slot = int(role.n) if role.n.isdigit() else len(arg_struct.args) - 1
                if role.vnroles:
                    for vnrole in role.vnroles:
                        arg = PlotPointArg(role.descr, role.f, vnrole.vntheta,
                                           self.verbnet.get_complete_class_id(vnrole.vncls), slot, False, dataset)
                        arg_struct.add_arg(arg)
                else:
                    arg = PlotPointArg(role.descr, role.f, '', '', slot, False, dataset)
                    arg_struct.add_arg(arg)
        elif dataset == Dataset.VN:
            id = self.verbnet.get_complete_class_id(id)
            arg_struct = PlotPointArgStruct(id, dataset)
            for i, role in enumerate(roles):
                arg = PlotPointArg('', '', role.value, id, int(role.slot), role.implicit, dataset)
                arg_struct.add_arg(arg)

        return arg_struct


class CompiledPlotPoint(object):
    ...


@dataclass
class PlotPointPredicateArg:
    type: str
    value: str

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}value={self.value!r}{end}'

    def __iter__(self):
        yield 'type', self.type
        yield 'value', self.value


@dataclass
class PlotPointArg:
    descr: str = ''
    type: str = ''
    value: str = ''
    cls: str = ''
    slot: int = -1
    implicit: bool = False
    dataset: str = Dataset.EMPTY

    def fill_dict(self, dict):
        self.descr = dict.get('descr', '')
        self.type = dict.get('type', '')
        self.value = dict.get('value', '')
        self.cls = dict.get('cls', '')
        self.slot = dict.get('slot', -1)
        self.implicit = bool(dict.get('implicit', 'false'))
        self.dataset = dict.get('dataset', Dataset.EMPTY)

    def pred_dict(self):
        return {'type': self.type, 'value': self.value}

    def combine(self, arg):
        self.descr = arg.descr if self.descr == '' else self.descr
        self.type = arg.type if self.type == '' else self.type
        self.value = arg.value if self.value == '' else self.value
        self.cls = arg.cls if self.cls == '' else self.cls
        self.slot = arg.slot if self.slot == -1 else self.slot
        self.implicit = arg.implicit if not self.implicit else self.implicit
        self.dataset = Dataset.PP

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
        yield 'dataset', self.dataset

    def __str__(self):
        return f'{self.type}: {self.value}'


@dataclass
class PlotPointPredicate:
    bool: str
    name: str
    args: List[PlotPointArg] = field(default_factory=list)

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}bool={self.bool!r}{end}' \
               f'{indent_}name={self.name!r}{end}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint_pred(indent + 2, end) for arg in self.args])}'

    def __iter__(self):
        yield 'bool', self.bool
        yield 'name', self.name
        yield 'args', [arg.pred_dict() for arg in self.args]


@dataclass
class PlotPointArgStruct:
    id: str
    dataset: str
    args: List[PlotPointArg] = field(default_factory=list)

    def add_arg(self, pp_arg):
        self.args.append(pp_arg)

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
class PlotPointExample:
    wn: list = field(default_factory=list)
    vn: list = field(default_factory=list)
    fn: list = field(default_factory=list)
    gr: list = field(default_factory=list)
    pb: list = field(default_factory=list)

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
    id: str
    dataset: str
    descr: str
    mappings: PlotPointMapping = field(default_factory=PlotPointMapping)
    examples: PlotPointExample = field(default_factory=PlotPointExample)
    arg_structs: List[PlotPointArgStruct] = field(default_factory=list)
    args: List[PlotPointArg] = field(default_factory=list)

    def add_arg_struct(self, pp_args):
        self.arg_structs.append(pp_args)

    def squeeze(self):
        args = []
        for arg_struct in self.arg_structs:
            for arg_x in arg_struct.args:
                args.append(arg_x)

        args.sort(key=lambda x: str(x.slot), reverse=False)

        while len(args) != 0:
            arg_x = args[0]
            lst = args
            for i, arg_y in enumerate(lst):
                if arg_y != arg_x:
                    if (arg_y.type == '' or arg_x.type == '') and arg_y.value == arg_x.value and arg_y.cls == arg_x.cls:
                        arg_x.combine(arg_y)
                        args.pop(i)

            self.args.append(arg_x)
            args.pop(0)

        self.args.sort(key=lambda x: str(x.slot), reverse=False)

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

    def __iter__(self):
        yield 'id', self.id
        yield 'dataset', self.dataset
        yield 'descr', self.descr
        yield 'mappings', dict(self.mappings)
        yield 'examples', dict(self.examples)
        yield 'arg_structs', [dict(arg) for arg in self.arg_structs]
        yield 'args', [dict(arg) for arg in self.args]

    def __str__(self):
        return f'{self.id}: {str(self.dataset)}: {str(self.descr)}'


@dataclass
class PlotPoint:
    ''' A data class that stores the senses of plot points and selects the sense'''
    lemma: str
    type: PlotPointType = PlotPointType.VERB
    selected: PlotPointSense = None
    dataset: str = ''
    aligned: bool = False
    senses: List[PlotPointSense] = field(default_factory=list)

    def add_sense(self, pp_sense):
        self.senses.append(pp_sense)

    def pprint(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}lemma={self.lemma!r}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}selected={self.selected!r}{end}' \
               f'{indent_}dataset={self.dataset!r}{end}' \
               f'{indent_}aligned={str(self.aligned)!r}{end}' \
               f'{indent_}senses={end}' \
               f'{"".join([sense.pprint(indent + 1) for sense in self.senses])}'

    def __iter__(self):
        yield 'lemma', self.lemma
        yield 'type', self.type
        yield 'selected', self.selected
        yield 'dataset', self.dataset
        yield 'aligned', self.aligned
        yield 'senses', [dict(sense) for sense in self.senses]


if __name__ == '__main__':
    vn = PlotPointContainer()
    # verbs = vn.get_verbs()
