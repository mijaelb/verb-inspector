# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:51:21 2019

@author: Mijael
"""
import bs4
import re
import json
import os
import sys
from pathlib import Path
from itertools import chain
from collections import Counter
from utils import utils


class VerbNet(object):
    def __init__(self, path=''):
        self.path = Path(path)
        self.files_soup = self.parse()
        self.verb_classes = self.get_verb_classes()
        self.lemmas = self.get_lemmas()

    def parse(self):
        return utils.parse_xmls(self.path, 'lxml-xml')

    def get_verb_classes(self, class_ids=[]):
        verb_classes = getattr(self, 'verb_classes', {})
        if not verb_classes:
            # Extract every VNCLASS and VNSUBCLASS into a VerbClass object
            for filename, soup in self.files_soup.items():
                verb_classes[soup.VNCLASS.attrs['ID']] = VerbNetClass(filename, soup.VNCLASS)
                for vnsubclass in soup.find_all('VNSUBCLASS'):
                    verb_classes[vnsubclass.attrs['ID']] = VerbNetClass(filename, vnsubclass)

        if class_ids:
            verb_classes = {class_id: verb_classes[class_id] for class_id in class_ids}

        return verb_classes

    def get_lemmas(self):
        lemmas = getattr(self, 'lemmas', [])
        if not lemmas:
            for verb_class in self.verb_classes:
                for member in verb_class.members:
                    lemmas.append(member.name


    def __str__(self):
        return str(self.verb_classes.keys())


class VerbNetClass(object):
    def __init__(self, filename='', soup=None):
        self.soup = soup
        self.filename = filename
        self.id = soup.attrs['ID']
        self.frames = self.get_frames()
        self.themroles = self.get_themroles()
        self.all_preds = self.get_all_preds()
        self.all_args = self.get_all_args()
        self.members = self.get_members()
        # print("'" + self.id + "':" + ''.join([' ' for i in range(len("'" + self.id + "':"), 40)]) + str(self.class_args) + ",")

    def get_themroles(self):
        themroles = getattr(self, 'themroles', [])
        if not themroles:
            for themrole in self.soup.THEMROLES.find_all('THEMROLE'):
                role = utils.norm_role(themrole.attrs)
                selrestrs = themrole.find_all('SELRESTRS')

                selrestrs_dict = selrestrs.attrs if hasattr(selrestrs, 'attrs') else {}
                selrestrs_dict['selrestrs'] = []
                for selrestr in themrole.find_all('SELRESTR'):
                    selrestrs_dict['selrestrs'].append(utils.norm(selrestr.attrs))

                themroles.append({'type': role['type'], 'selrestrs': selrestrs_dict})

        return themroles

    def get_frames(self):
        frames = getattr(self, 'frames', [])
        if not frames:
            for frame in self.soup.FRAMES.find_all('FRAME'):
                frames.append(VerbNetFrame(self.id, self.filename, frame))

        return frames

    def get_members(self):
        members = getattr(self, 'members', [])
        if not members:
            for member in self.soup.MEMBERS.find_all('MEMBER'):
                for key in member.attrs:
                    member.attrs[key] = member.attrs[key].split()
                members.append(member.attrs)
        return members

    def get_all_args(self):
        pred_args = []
        syntax_args = []
        themrole_args = [role['type'] for role in self.themroles]

        for frame in self.frames:
            pred_args.extend(frame.get_pred_args())
            syntax_args.append(frame.get_syntax_args())

        class_args = pred_args + syntax_args
        flatten = lambda l: [item for sublist in l for item in sublist]
        class_args = list(dict.fromkeys(Counter(flatten(class_args))))

        # Consider the predicate equals to group arguments
        # for example equals(recipient, stimulus) means [recipient, stimulus]
        # inside the general argument structure of the class
        for pred in self.class_preds:
            if pred.name == 'equals':
                group = []
                for arg in pred.args:
                    if arg != 'event' and arg != 'constant':
                        group.append(arg['value'])

                remove = False
                for i, arg in enumerate(class_args):
                    if any([arg == group_arg for group_arg in group]):
                        if not remove:
                            class_args[i] = group
                            remove = True
                        else:
                            del class_args[i]

        return class_args

    def get_all_preds(self):
        preds = []
        for frame in self.frames:
            for pred in frame.preds:
                if not any([str(pred) == str(pr) for pr in preds]):
                    preds.append(pred)
        return preds


class VerbNetFrame(object):
    def __init__(self, class_id, filename, soup):
        self.class_id = class_id
        self.filename = filename
        self.soup = soup
        self.descr = soup.DESCRIPTION.attrs
        self.primary = self.descr['primary']
        self.secondary = '' if 'secondary' not in self.descr else self.descr['secondary']
        self.xtag = self.descr['xtag']
        self.descr_num = self.descr['descriptionNumber']
        self.example = ' '.join(soup.find_all('EXAMPLE')[0].text.split())
        self.syntax = self.get_syntax()
        self.preds = self.get_preds()
        self.syntax_args = self.get_syntax_args()
        self.pred_args = self.get_pred_args()

    def get_syntax(self):
        syntax = getattr(self, 'syntax', [])
        if not syntax:
            for stx in self.soup.SYNTAX.find_all(['NP', 'VERB', 'PREP']):
                stx_dict = {'tag': stx.name,
                            'value': utils.norm_role(stx.attrs.get('value', '').replace('|', ' ').split()),
                            'synrestrs': [],
                            'selrestrs': []}

                for synrestr in stx.find_all('SYNRESTR'):
                    stx_dict['synrestrs'].append(utils.norm(synrestr.attrs))

                for selrestr in stx.find_all('SELRESTR'):
                    stx_dict['selrestrs'].append(utils.norm(selrestr.attrs))

                syntax.append(stx_dict)

        return syntax

    def get_syntax_args(self):
        syntax_args = getattr(self, 'syntax_args', [])
        if not syntax_args:
            for stx in self.syntax:
                if stx['tag'] == 'NP':
                    syntax_args.append(stx['value'][0])

        return syntax_args

    def get_pred_args(self):
        pred_args = getattr(self, 'pred_args', [])
        if not pred_args:
            for pred in self.preds:
                pred_args.append(pred.get_role_args())

        return pred_args

    def get_preds(self):
        preds = getattr(self, 'preds', [])
        if not preds:
            for pred in self.soup.SEMANTICS.find_all('PRED'):
                preds.append(VerbNetPredicate(pred))

        return preds


class VerbNetPredicate(object):
    def __init__(self, soup=None):
        self.soup = soup
        self.bool = '' if 'bool' not in soup.attrs else soup.attrs['bool']
        self.name = soup.attrs['value']
        self.args = self.get_args()

    def add_arg(self, type, value, idx=-1):
        self.args.insert(idx, {'type': type, 'value': value})

    def get_args(self):
        ''' '''
        args = getattr(self, 'args', [])
        if self.soup:
            if not args:
                for arg in self.soup.ARGS.find_all('ARG'):
                    # ** There is one case in admire-31.2.xml that a value appears as 'Stimulus, Attribute'
                    # in the predicate. I do not know if they will remove this in the future. The next
                    # piece of code is to be able to generalize to those kind of cases
                    for role in arg.attrs['value'].split(','):
                        args.append({'type': utils.norm(arg.attrs['type']), 'value': utils.norm_role(role)})

        return args

    def get_role_args(self):
        role_args = []
        for arg in self.args:
            if arg['type'] != 'event' and arg['type'] != 'constant':
                role_args.append(arg['value'])
        return role_args

    def __str__(self):
        return self.bool + self.name + '(' + ','.join([str(arg['value']) for arg in self.args]) + ')'


# class Verb(object):
#     def __init__(self, name):
#         self.name = name
#         self.senses = []
#         ...
#
#     def add_verb_sense(self, class_id, groupings=[], fnframes=[], wn=[]):
#         ...
#         # sense = VerbSense(self.name, )
#         # self.senses
#
#     def __str__(self):
#         return self.lemma
#
#
# class VerbSense(Predicate):
#     def __init__(self, name, id):
#         super.__init__(name)
#         self.id = id


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'corpora/verbnet/')
    vn = VerbNet(filename)
    # verbs = vn.get_verbs()
