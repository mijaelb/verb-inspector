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
verbnet_simplified_path = os.path.join(dirname, 'data/verbnet_simplified.json')


class PlotPointContainer(object):
    def __init__(self, json_path=''):
        self.json_path = json_path
        self.verbnet = vn.VerbNet(verbnet_path)
        self.verbnet_simplified = vn.VerbNetSimplified(self.verbnet, '')
        # self.vnpb = utils.fromjson(vnpb_path)
        # self.propbank = pb.PropBank(propbank_path)
        # self.groupings = gr.Groupings(groupings_path)
        self.bso = ''
        # self.plotpoints = self.get_plotpoints()

    def get_plotpoints(self):
        plotpoints = getattr(self, 'plotpoints', [])
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
                pps = {}
                for lemma, datasets in lemmas.items():
                    pps[lemma] = PlotPoint(lemma, PlotPointType.VERB)
                    if Dataset.GR in datasets:
                        senses = self.groupings.get_senses(lemma)
                        for sense in senses.values():
                            pp_sense = self.get_sense_grouping(lemma, sense)
                            pps[lemma].add_sense(pp_sense)

                    if Dataset.PB in datasets:
                        rolesets = self.propbank.get_rolesets(lemma)
                        for roleset in rolesets:
                            pp_sense = self.get_sense_propbank(lemma, roleset)
                            pps[lemma].add_sense(pp_sense)

                    if Dataset.VN in datasets:
                        classes = self.verbnet.get_classes(lemma)
                        for cls in classes.values():
                            pp_class = self.get_class_verbnet(cls, lemma)
                            pps[lemma].add_sense(pp_class)

                    utils.write('pps.log', pps[lemma].pprint(), 'a+')
                # utils.tojson('pps', pps)
        return plotpoints

    def get_class_verbnet(self, cls, lemma):
        pp_sense = PlotPointSense(cls.id, Dataset.VN, '')
        pp_sense.mappings.wn = cls.get_member(lemma).wn
        pp_sense.mappings.vn = [cls.id]
        pp_sense.mappings.pb = [roleset.id for roleset in self.propbank.get_rolesets_from_class(cls.id, lemma)]
        pp_sense.mappings.gr = cls.get_member(lemma).grouping
        pp_sense.mappings.fn = cls.get_member(lemma).fnframe
        pp_sense.examples.vn = cls.get_examples()

        arg_struct = self.get_args_verbnet(cls.id)
        if arg_struct:
            pp_sense.add_args(arg_struct)

        return pp_sense

    def get_sense_propbank(self, lemma, roleset):
        pp_sense = PlotPointSense(roleset.id, Dataset.PB, roleset.name)
        pp_sense.mappings.wn = []
        pp_sense.mappings.vn = roleset.get_classes()
        pp_sense.mappings.pb = [roleset.id]
        gr_senses = self.groupings.get_senses_from_pb(lemma, roleset)
        pp_sense.mappings.gr = [sense.id for sense in gr_senses]
        pp_sense.mappings.fn = []
        pp_sense.examples.pb = [example.text for example in roleset.examples]

        arg_struct = self.get_args_propbank(roleset.id)
        if arg_struct:
            pp_sense.add_args(arg_struct)

        for class_id in pp_sense.mappings.vn:
            arg_struct = self.get_args_verbnet(class_id)
            if arg_struct:
                pp_sense.add_args(arg_struct)

        return pp_sense

    def get_sense_grouping(self, lemma, sense):
        pp_sense = PlotPointSense(sense.id, Dataset.GR, sense.name)
        pp_sense.mappings.wn = sense.mappings.wn
        gr_vn = [cls.id for cls in self.verbnet.get_classes_from_gr(lemma, sense.id).values()]
        pp_sense.mappings.vn = list(dict.fromkeys(sense.mappings.vn + gr_vn))
        pp_sense.mappings.pb = sense.mappings.pb
        pp_sense.mappings.gr = [sense.id]
        pp_sense.mappings.fn = sense.mappings.fn
        pp_sense.examples.gr = sense.examples

        for roleset in pp_sense.mappings.pb:
            arg_struct = self.get_args_propbank(roleset)
            if arg_struct:
                pp_sense.add_args(arg_struct)

        for class_id in pp_sense.mappings.vn:
            arg_struct = self.get_args_verbnet(class_id)
            if arg_struct:
                pp_sense.add_args(arg_struct)

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
        arg_struct = PlotPointArgStruct(id, dataset)
        if dataset == Dataset.PB:
            for role in roles:
                arg = PlotPointArg(role.descr, role.n)
                if role.vnroles:
                    for vnrole in role.vnroles:
                        arg.add_role(role.f, vnrole.vntheta, vnrole.vncls, dataset)
                else:
                    arg.add_role(role.f, '', '', dataset)

                arg_struct.add_arg(arg)
        elif dataset == Dataset.VN:
            for i, role in enumerate(roles):
                arg = PlotPointArg('', i)
                if isinstance(role, list):
                    for theta in role:
                        arg.add_role(theta, theta, id, dataset)
                else:
                    arg.add_role(role, role, id, dataset)

                arg_struct.add_arg(arg)

        return arg_struct


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


@dataclass
class PlotPointPredicate:
    bool: str
    name: str
    args: List[PlotPointPredicateArg] = field(default_factory=list)

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}bool={self.bool!r}{end}' \
               f'{indent_}name={self.name!r}{end}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint(indent + 2, end) for arg in self.args])}'


@dataclass
class PlotPointRole:
    role: str
    themrole: str
    vnclass: str
    dataset: str

    def pprint(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}role={self.role}{end}' \
               f'{indent_}themrole={self.themrole}{end}' \
               f'{indent_}vnclass={self.vnclass}{end}' \
               f'{indent_}dataset={self.dataset}{end}'


@dataclass
class PlotPointArg:
    descr: str
    arg: str
    roles: List[PlotPointRole] = field(default_factory=list)

    def add_role(self, role, themrole, vnclass, dataset):
        self.roles.append(PlotPointRole(role, themrole, vnclass, dataset))

    def pprint(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}descr={self.descr}{end}' \
               f'{indent_}arg={self.arg}{end}' \
               f'{indent_}roles={end}' \
               f'{"".join([role.pprint(indent + 2) for role in self.roles])}'


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


@dataclass
class PlotPointSense:
    id: str
    dataset: str
    descr: str
    mappings: PlotPointMapping = field(default_factory=PlotPointMapping)
    examples: PlotPointExample = field(default_factory=PlotPointExample)
    args: List[PlotPointArgStruct] = field(default_factory=list)

    def add_args(self, pp_args):
        self.args.append(pp_args)

    def pprint(self, indent=0, end='\n'):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}id={self.id!r}{end}' \
               f'{indent_}dataset={self.dataset!r}{end}' \
               f'{indent_}descr={self.descr!r}{end}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint(indent + 2) for arg in self.args])}' \
               f'{indent_}mappings={end}' \
               f'{self.mappings.pprint(indent + 2)}' \
               f'{indent_}examples={end}' \
               f'{self.examples.pprint(indent + 2)}'


@dataclass
class PlotPoint:
    ''' A data class that stores the senses of plot points and selects the sense'''
    lemma: str
    type: PlotPointType = PlotPointType.VERB
    selected: str = ''
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


if __name__ == '__main__':
    vn = PlotPointContainer()
    # verbs = vn.get_verbs()
