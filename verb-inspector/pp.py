import bs4
import re
import json
import os
import sys
from pathlib import Path
from itertools import chain
from collections import Counter
from utils import utils
import gr
import pb
import vn

Dataset = utils.enum('VN', 'PB', 'GR', 'FN', 'EMPTY')
PlotPointType = utils.enum('VERB', 'PREP', 'EMPTY')

dirname = os.path.dirname(__file__)
groupings_path = os.path.join(dirname, 'corpora/ontonotes/sense-inventories/')
propbank_path = os.path.join(dirname, 'corpora/propbank/frames/')
verbnet_path = os.path.join(dirname, 'corpora/verbnet/')


class PlotPointContainer(object):
    def __init__(self, json_path=''):
        self.json_path = json_path
        self.verbnet = vn.VerbNet(verbnet_path)
        self.propbank = pb.PropBank(propbank_path)
        self.groupings = gr.Groupings(groupings_path)
        self.plotpoints = self.get_plotpoints()

    def get_plotpoints(self):
        plotpoints = getattr(self, 'plotpoints', [])
        if not plotpoints:
            if self.json_path:
                pps_dict = utils.fromjson(self.json_path)
            else:
                pps_dict = self.create_plotpoints_dict()
            # for lemma, pp_dict in pps_dict.items():
            #     plotpoints.append(PlotPoint(lemma,
            #                                 pp_dict))
        return plotpoints

    def create_plotpoints_dict(self, priority=[Dataset.GR, Dataset.PB]):
        #roles = self.format_roles(self.propbank.get_roles('abduct.01'), Dataset.PB)
        #classes = self.propbank.get_vnclasses('abduct.01')
        vnclasses = self.verbnet.get_classes('move')
        rolesets = self.propbank.get_rolesets('move')
        roleset = self.propbank.get_roleset('move.01')
        classes = self.propbank.get_vnclasses('move.01')
        print(classes)
        print(roleset.name)
        #classes = self.
        print(vnclasses)
        print(str(rolesets))
        print(str(roleset))
        #print(classes)
        #print(roles)
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

    def format_roles(self, roles, dataset):
        args = []
        if dataset == Dataset.PB:
            for role in roles:
                arg = {'descr': role['descr'], 'n': role['n'], 'roles': []}
                if role['vnroles']:
                    for vnrole in role['vnroles']:
                        arg['roles'].append({'role': role['f'], 'themrole': vnrole['vntheta'], 'vnclass': vnrole['vncls']})
                else:
                    arg['roles'].append({'role': role['f'], 'themrole': '', 'vnclass': ''})
                args.append(arg)
        elif dataset == Dataset.VN:
            ...

        return args


class PlotPoint(object):
    ''' A class that stores the senses of plot points and select'''

    def __init__(self, lemma, pp_dict):
        '''

        Args:
            lemma:
            pp_dict:
        '''
        self.lemma = lemma
        self.pp_dict = pp_dict
        self.predicates = self.get_predicates()
        self.selected_sense = self.get_selected_sense()

    def get_predicates(self):
        predicates = getattr(self, 'predicates', [])
        if not predicates:
            for sense, sense_dict in self.pp_dict:
                predicates.append(PlotPointPredicate(self.lemma,
                                                     sense,
                                                     sense_dict['args'],
                                                     sense_dict['vnclasses'],
                                                     sense_dict['dataset'],
                                                     sense_dict['type']))
        return predicates

    def get_selected_sense(self):
        selected_sense = getattr(self, 'selected_sense', None)
        if not selected_sense:
            selected_sense = self.pp_dict['selected']

        return selected_sense


class PlotPointPredicate(object):
    """ A class that contains the general argument structure and the sense of a predicate for a certain plot point """

    def __init__(self, lemma, sense, args, vnclasses, from_dataset=Dataset.EMPTY, type=PlotPointType.VERB):
        """
            Argument structure of the plot point predicate is defined as a list of PlotPointArg objects
            [ [ { vnrole: 'agent', vncls: 'class-1.1' }, ... ], [ { ... , ... } ], [ { ... , ... , ... } ] ]
            [ ARG0, ARG1, ARG2, ARG3, ..., ARGN ]

            Each index of the outer list corresponds to the argument position in the predicate
            In case of verbs: subject, direct object, indirect object and additional arguments.
            The arguments are thematic roles from to classes of verbnet, they correspond to the arguments as
            required in the frame predicates.

            There are two types of predicates for a plot point.
                PlotPoint.VERB verb predicate (e.g. go, move, eat, etc.)
                PlotPointType.PREP spatial preposition (e.g. on, in, at, into, etc.)

            Args:
                lemma:
                sense:
                args:
                vnclasses:
                dataset:
                type:
        """
        if type.capitalize() not in (PlotPointType.VERB, PlotPointType.PREP, PlotPointType.EMPTY):
            raise ValueError("Plot point type '" + str(type) + "' not valid")
        if from_dataset.capitalize() not in (PlotPointType.GR, PlotPointType.PB, PlotPointType.FN, PlotPointType.EMPTY):
            raise ValueError("Plot point sense dataset '" + str(from_dataset) + "' not valid")

        self.lemma = lemma
        self.sense = sense
        self.vnclasses = vnclasses
        self.from_dataset = from_dataset
        self.type = type
        self.args = args


class PlotPointArg(object):
    def __init__(self, descr, n):
        self.descr = descr
        self.n = n
        self.roles = []

    def add_role(self, role, themrole, vnclass, dataset):
        """
        This adds possible roles in

        Arg:
            role:
            themrole:
            vnclass:
            dataset:
        """
        self.roles.append({'role': role,
                           'themrole': themrole,
                           'vnclass': vnclass,
                           'dataset': dataset})

class PlotPointRole(object):
    ...


if __name__ == '__main__':
    vn = PlotPointContainer()
    # verbs = vn.get_verbs()
