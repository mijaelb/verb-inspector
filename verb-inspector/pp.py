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
    EMPTY = ''


class PlotPointType(Enum):
    VERB = 'verb'
    PREP = 'prep'
    EMPTY = ''


# Dataset = utils.enum('VN', 'PB', 'GR', 'FN', 'EMPTY')
# PlotPointType = utils.enum('VERB', 'PREP', 'EMPTY')

dirname = os.path.dirname(__file__)
groupings_path = os.path.join(dirname, 'corpora/ontonotes/sense-inventories/')
propbank_path = os.path.join(dirname, 'corpora/propbank/frames/')
verbnet_path = os.path.join(dirname, 'corpora/verbnet/')
vnpb_path = os.path.join(dirname, 'corpora/mappings/vnpb-mappings.json')

class_name_typos = { 'judgement': 'judgment',
                     'occurrence': 'occur',
                     'crave': 'carve',
                     'spacial_configuration': 'spatial_configuration',
                     'clasify': 'classify',
                     'contguous_location': 'contiguous_location',
                     'modes_of_being_with_mothion': 'modes_of_being_with_motion',
                     'noverbal_expression': 'nonverbal_expression',
                     'skid': 'run',
                     'temporal_configuration': 'occur',
                     'approve': 'accept',
                     'sastify': 'satisfy'}

class_name = { 'settle-89':  ['harmonize-22.6', 'acquiesce-95.1-1', 'hire-13.5.3'],
               'force-59':   ['urge-58.1-1-1', 'compel-59.1', 'stimulate-59.4', 'trick-59.2', 'urge-58.1-1'],
               'force-59.1': ['compel-59.1'],
               'force-59-1': ['compel-59.1', 'trick-59.2']}

class PlotPointContainer(object):
    def __init__(self, json_path=''):
        self.json_path = json_path
        self.verbnet = vn.VerbNet(verbnet_path)
        self.vnpb = utils.fromjson(vnpb_path)
        self.propbank = pb.PropBank(propbank_path)
        self.groupings = gr.Groupings(groupings_path)

        self.plotpoints = self.get_plotpoints()

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
                            #print('--------------------------------------------------------------------------------')
                            #print(pp_sense.pprint())
                            #print('--------------------------------------------------------------------------------')
                            pps[lemma].add_sense(pp_sense)

                    #if Dataset.PB in datasets:
                        #rolesets = self.propbank.get_rolesets(lemma)
                        #for roleset in rolesets:
                           #pp_sense = self.get_sense_propbank(lemma, roleset)
                            #print('--------------------------------------------------------------------------------')
                            #print(pp_sense.pprint())
                            #print('--------------------------------------------------------------------------------')
                            #pps[lemma].add_sense(pp_sense)

        return plotpoints

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
            arg_struct = self.get_args_verbnet(class_id, lemma, roleset.id)
            if arg_struct:
                pp_sense.add_args(arg_struct)

        return pp_sense

    def get_sense_grouping(self, lemma, sense):
        pp_sense = PlotPointSense(sense.id, Dataset.GR, sense.name)
        pp_sense.mappings.wn = sense.mappings.wn
        pp_sense.mappings.vn = sense.mappings.vn
        pp_sense.mappings.pb = sense.mappings.pb
        pp_sense.mappings.gr = [sense.id]
        pp_sense.mappings.fn = sense.mappings.fn
        pp_sense.examples.gr = sense.examples

        for roleset in sense.mappings.pb:
            arg_struct = self.get_args_propbank(roleset)
            if arg_struct:
                pp_sense.add_args(arg_struct)

        for class_id in sense.mappings.vn:
            arg_struct = self.get_args_verbnet(class_id, lemma, sense.id)
            if arg_struct:
                pp_sense.add_args(arg_struct)
            else:
                self.clean_groupings(class_id, lemma, sense.id)

        return pp_sense

    def get_args_propbank(self, roleset):
        roles = self.propbank.get_roles(roleset)
        if roles:
            arg_struct = self.transform_roles(roles, roleset, Dataset.PB)
            return arg_struct
        return None

    def get_args_verbnet(self, class_id, lemma='', roleset=''):
        cls = self.verbnet.get_class(class_id)
        if cls:
            args = cls.get_all_args()
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

    def clean_groupings(self, class_id, lemma, sense):
        classes = list(self.verbnet.get_classes(lemma).keys())
        print(sense + ' ' + lemma + ' Not found: ' + class_id)
        print(classes)
        tupl = re.match(r'(\w+)-(.*)', class_id)
        if tupl:
            cls, id = (tupl[1], tupl[2])
            id_ = re.sub(r'-\d', '', id)
            res = ''
            print(cls + ' ' + id)
            if class_id in class_name:
                for cls_id in class_name[class_id]:
                    if cls_id in classes:
                        res = cls_id
                        print(f'{class_id} is {res}')
                        break

            if not res:
                for cls_id in classes:
                    if cls in class_name_typos:
                        cls = class_name_typos[cls]

                    if cls in cls_id:
                        res = cls_id
                        print(f'{class_id} is {res}')
                        break

            if not res:
                if class_id in class_name:
                    for cls_id in class_name[class_id]:
                        if cls_id in self.verbnet.classes:
                            res = cls_id
                            print(f'{class_id} is {res}')
                            break

            if not res:
                for cls_id in self.verbnet.classes:
                    if cls in class_name_typos:
                        cls = class_name_typos[cls]

                    tupl = re.match(r'(\w+)-(.*)', cls_id)
                    if cls == tupl[1]:
                        res = cls_id
                        print(f'{class_id} is {res}')
                        break

            if not res:
                for cls_id in classes:
                    if id in cls_id or id_ in cls_id:
                        res = cls_id
                        print(f'{class_id} is {res}')
                        break

            if not res:
                for cls_id in self.verbnet.classes:
                    if '-'+id in cls_id or '-'+id_ in cls_id:
                        res = cls_id
                        print(f'{class_id} is {res}')
                        break

            if not res and len(classes) == 1:
                res = classes[0]
                print(f'{class_id} is {res}')

        if res:
            if self.query_yes_no('Edit?'):
                self.groupings.replace(class_id, res, lemma)


    def query_yes_no(self, question, default="yes"):
        valid = {"yes": True, "y": True, "ye": True,
                 "no": False, "n": False}
        if default is None:
            prompt = " [y/n] "
        elif default == "yes":
            prompt = " [Y/n] "
        elif default == "no":
            prompt = " [y/N] "
        else:
            raise ValueError("invalid default answer: '%s'" % default)

        while True:
            sys.stdout.write(question + prompt)
            choice = input().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' "
                                 "(or 'y' or 'n').\n")

    def create_plotpoints_dict(self, priority=[Dataset.GR, Dataset.PB]):
        senses = self.groupings.get_pb_ids('move')
        classes = self.groupings.get_vn_classes('move')
        print(senses)
        print(classes)
        roles = self.get_roles(self.propbank.get_roles('abduct.01'), Dataset.PB)
        # classes = self.propbank.get_vnclasses('abduct.01')
        mappings = self.groupings.get_senses('move')
        # print(mappings)
        vnclasses = self.verbnet.get_classes('move')
        rolesets = self.propbank.get_rolesets('move')
        roleset = self.propbank.get_roleset('move.01')
        classes = self.propbank.get_vnclasses('move.01')

        # print(roles)
        # print(classes)
        # print(roleset.name)
        # classes = self.
        # print(vnclasses)
        # print(str(rolesets))
        # print(str(roleset))
        # print(classes)
        # print(roles)
        lemmas = {utils.norm(lemma): [Dataset.VN] for lemma in self.verbnet.get_lemmas()}
        lemmas = utils.deep_update(lemmas, {utils.norm(lemma): [Dataset.PB] for lemma in self.propbank.get_lemmas()})
        lemmas = utils.deep_update(lemmas, {utils.norm(lemma): [Dataset.GR] for lemma in self.groupings.get_lemmas()})
        print(len(lemmas))
        print(lemmas)
        # pps_dict = {}
        # for lemma, datasets in lemmas.items():
        #     pps_dict[lemma] = []
        #     if Dataset.GR in datasets:
        #         gr_senses = self.groupings.get_senses(lemma)
        #         for sense in gr_senses:
        #             sense_dict = {}
        #             sense_dict['id'] = sense.id
        #             sense_dict['dataset'] = 'gr'
        #             sense_dict['verbnet'] = sense.get_verbnet_mappings()
        #             sense_dict['propbank'] = sense.get_propbank_mappings()
        #             sense_dict['args'] = []
        #
        #             # Get argument structure proposal from propbank
        #             if sense_dict['propbank']:
        #                 for pb_sense in sense_dict['propbank']:
        #                     def
        #
        #             pps_dict[lemma].append(sense_dict)
        #

        # print(len(lemmas))
        # print(lemmas)
        ...


# class PlotPoint(object):
#     ''' A class that stores the senses of plot points and select'''
#
#     def __init__(self, lemma, pp_dict):
#         self.lemma = lemma
#         self.pp_dict = pp_dict
#         self.predicates = self.get_predicates()
#         self.selected_sense = self.get_selected_sense()
#
#     def get_predicates(self):
#         predicates = getattr(self, 'predicates', [])
#         if not predicates:
#             for sense, sense_dict in self.pp_dict:
#                 predicates.append(PlotPointPredicate(self.lemma,
#                                                      sense,
#                                                      sense_dict['args'],
#                                                      sense_dict['vnclasses'],
#                                                      sense_dict['dataset'],
#                                                      sense_dict['type']))
#         return predicates
#
#     def get_selected_sense(self):
#         selected_sense = getattr(self, 'selected_sense', None)
#         if not selected_sense:
#             selected_sense = self.pp_dict['selected']
#
#         return selected_sense


# class PlotPointPredicate(object):
#     """ A class that contains the general argument structure and the sense of a predicate for a certain plot point """
#
#     def __init__(self, lemma, sense, args, vnclasses, from_dataset=Dataset.EMPTY, type=PlotPointType.VERB):
#         """
#             Argument structure of the plot point predicate is defined as a list of PlotPointArg objects
#             [ [ { vnrole: 'agent', vncls: 'class-1.1' }, ... ], [ { ... , ... } ], [ { ... , ... , ... } ] ]
#             [ ARG0, ARG1, ARG2, ARG3, ..., ARGN ]
#
#             Each index of the outer list corresponds to the argument position in the predicate
#             In case of verbs: subject, direct object, indirect object and additional arguments.
#             The arguments are thematic roles from to classes of verbnet, they correspond to the arguments as
#             required in the frame predicates.
#
#             There are two types of predicates for a plot point.
#                 PlotPoint.VERB verb predicate (e.g. go, move, eat, etc.)
#                 PlotPointType.PREP spatial preposition (e.g. on, in, at, into, etc.)
#
#             Args:
#                 lemma:
#                 sense:
#                 args:
#                 vnclasses:
#                 dataset:
#                 type:
#         """
#         if type.capitalize() not in (PlotPointType.VERB, PlotPointType.PREP, PlotPointType.EMPTY):
#             raise ValueError("Plot point type '" + str(type) + "' not valid")
#         if from_dataset.capitalize() not in (PlotPointType.GR, PlotPointType.PB, PlotPointType.FN, PlotPointType.EMPTY):
#             raise ValueError("Plot point sense dataset '" + str(from_dataset) + "' not valid")
#
#         self.lemma = lemma
#         self.sense = sense
#         self.vnclasses = vnclasses
#         self.from_dataset = from_dataset
#         self.type = type
#         self.args = args

@dataclass
class PlotPointRole:
    role: str
    themrole: str
    vnclass: str
    dataset: str

    def todict(self):
        return {'role': self.role,
                'themrole': self.themrole,
                'vnclass': self.vnclass,
                'dataset': self.dataset}

    def pprint(self, indent=0):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        newline = '\n'
        return f'{indent_in}{self.__class__.__name__}{newline}' \
               f'{indent_}role={self.role}{newline}' \
               f'{indent_}themrole={self.themrole}{newline}' \
               f'{indent_}vnclass={self.vnclass}{newline}' \
               f'{indent_}dataset={self.dataset}{newline}'


@dataclass
class PlotPointArg:
    descr: str
    arg: str
    roles: List[PlotPointRole] = field(default_factory=list)

    def add_role(self, role, themrole, vnclass, dataset):
        self.roles.append(PlotPointRole(role, themrole, vnclass, dataset))

    def todict(self):
        return {'descr': self.descr,
                'arg': self.arg,
                'roles': [role.todict for role in self.roles]}

    def pprint(self, indent=0):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        newline = '\n'
        return f'{indent_in}{self.__class__.__name__}{newline}' \
               f'{indent_}descr={self.descr}{newline}' \
               f'{indent_}arg={self.arg}{newline}' \
               f'{indent_}roles={newline}' \
               f'{"".join([role.pprint(indent+2) for role in self.roles])}'


@dataclass
class PlotPointArgStruct:
    id: str
    dataset: str
    args: List[PlotPointArg] = field(default_factory=list)

    def add_arg(self, pp_arg):
        self.args.append(pp_arg)

    def tolist(self):
        return [arg.todict() for arg in self.args]

    def pprint(self, indent=0):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        newline = '\n'
        return f'{indent_in}{self.__class__.__name__}{newline}' \
               f'{indent_}id={self.id}{newline}' \
               f'{indent_}dataset={self.dataset}{newline}' \
               f'{indent_}args={newline}' \
               f'{"".join([arg.pprint(indent+2) for arg in self.args])}'


@dataclass
class PlotPointMapping:
    wn: list = field(default_factory=list)
    vn: list = field(default_factory=list)
    fn: list = field(default_factory=list)
    gr: list = field(default_factory=list)
    pb: list = field(default_factory=list)

    def pprint(self, indent=0):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        newline = '\n'
        return f'{indent_in}{self.__class__.__name__}{newline}' \
               f'{indent_}wn={self.wn!r}{newline}' \
               f'{indent_}vn={self.vn!r}{newline}' \
               f'{indent_}fn={self.fn!r}{newline}' \
               f'{indent_}gr={self.gr!r}{newline}' \
               f'{indent_}pb={self.pb!r}{newline}'


@dataclass
class PlotPointExample:
    wn: list = field(default_factory=list)
    vn: list = field(default_factory=list)
    fn: list = field(default_factory=list)
    gr: list = field(default_factory=list)
    pb: list = field(default_factory=list)

    def pprint(self, indent=0):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        newline = '\n'
        return f'{indent_in}{self.__class__.__name__}{newline}' \
               f'{indent_}wn={self.wn!r}{newline}' \
               f'{indent_}vn={self.vn!r}{newline}' \
               f'{indent_}fn={self.fn!r}{newline}' \
               f'{indent_}gr={self.gr!r}{newline}' \
               f'{indent_}pb={self.pb!r}{newline}'


@dataclass
class PlotPointSense:
    id: str
    dataset: str
    descr: str
    mappings: PlotPointMapping = PlotPointMapping()
    examples: PlotPointExample = PlotPointExample()
    args: List[PlotPointArgStruct] = field(default_factory=list)

    def add_args(self, pp_args):
        self.args.append(pp_args)

    def todict(self):
        return {'id': self.id,
                'dataset': self.dataset,
                'descr': self.descr,
                'examples': self.examples,
                'args': [arg.tolist() for arg in self.args]}

    def pprint(self, indent=0):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        newline = '\n'
        return f'{indent_in}{self.__class__.__name__}{newline}' \
               f'{indent_}id={self.id!r}{newline}' \
               f'{indent_}dataset={self.dataset!r}{newline}' \
               f'{indent_}descr={self.descr!r}{newline}' \
               f'{indent_}args={newline}' \
               f'{"".join([struct.pprint(indent + 2) for struct in self.args])}' \
               f'{indent_}mappings={newline}' \
               f'{self.mappings.pprint(indent + 2)}' \
               f'{indent_}examples={newline}' \
               f'{self.examples.pprint(indent + 2)}'


@dataclass
class PlotPoint:
    lemma: str
    type: PlotPointType = PlotPointType.VERB
    selected: str = ''
    dataset: str = ''
    senses: List[PlotPointSense] = field(default_factory=list)
    def add_sense(self, pp_sense):
        self.senses.append(pp_sense)

    def pprint(self, indent=0):
        indent_in = ''.join(['\t' for i in range(0, indent)])
        indent_ = ''.join(['\t' for i in range(0, indent + 1)])
        newline = '\n'
        return f'{indent_in}{self.__class__.__name__}{newline}' \
               f'{indent_}lemma={self.lemma!r}{newline}' \
               f'{indent_}type={self.type!r}{newline}' \
               f'{indent_}selected={self.selected!r}{newline}' \
               f'{indent_}dataset={self.dataset!r}{newline}' \
               f'{indent_}senses={newline}' \
               f'{"".join([sense.pprint(indent + 1) for sense in self.senses])}'


if __name__ == '__main__':
    vn = PlotPointContainer()
    # verbs = vn.get_verbs()
