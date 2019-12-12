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
from dataclasses import field, dataclass
from typing import List
from data import vnclass_args


class VerbNet(object):
    def __init__(self, path=''):
        self.path = Path(path)
        self.files_soup = self.parse()
        self.classes = self.get_classes()
        self.lemmas = self.get_lemmas()

    def parse(self):
        return utils.parse_xmls(self.path, 'lxml-xml')

    def replace(self, str_, forstr_, class_id):
        utils.replace(str_, forstr_, self.path / self.classes[class_id].filename)

    def get_classes(self, lemma='', class_ids=[]):
        classes = getattr(self, 'classes', {})
        if not classes:
            # Extract every VNCLASS and VNSUBCLASS into a VerbClass object
            for filename, soup in self.files_soup.items():
                classes[soup.VNCLASS.attrs['ID']] = VerbNetClass(filename, soup.VNCLASS)
                for vnsubclass in soup.find_all('VNSUBCLASS'):
                    classes[vnsubclass.attrs['ID']] = VerbNetClass(filename, vnsubclass)

        if class_ids:
            classes = {class_id: classes[class_id] for class_id in class_ids}

        if lemma:
            lemma_classes = {}
            for cls, obj in classes.items():
                for member in obj.members:
                    if member.name == lemma:
                        lemma_classes[cls] = obj
            classes = lemma_classes

        return classes

    def get_classes_from_gr(self, lemma, sense_id):
        classes = {}
        for cls, obj in self.classes.items():
            for member in obj.members:
                if sense_id in member.grouping:
                    classes[cls] = obj

        return classes

    def get_classes_ids(self):
        return list(self.classes.keys())

    def get_classes_name(self, lemma):
        classes = []
        for cls, obj in self.classes.items():
            for member in obj.members:
                if member.name == lemma:
                    classes.append(cls)
        return classes

    def get_class(self, class_id):
        if class_id in self.classes:
            return self.classes[class_id]
        else:
            for cls in self.classes:
                if '-' + class_id in cls:
                    return self.classes[cls]
        return None

    def get_lemmas(self):
        lemmas = getattr(self, 'lemmas', [])
        if not lemmas:
            for cls, obj in self.classes.items():
                for member in obj.members:
                    lemmas.append(member.name)
        return list(dict.fromkeys(lemmas))

    def get_args(self, class_id):
        cls = self.get_class(class_id)
        return cls.get_all_args()

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}path={self.path!r}{end}' \
               f'{indent_}classes={end}' \
               f'{"".join([cls.pprint(indent + 2, end) for cls in self.classes.values()])}'

    def __str__(self):
        return str(self.classes.keys())


class VerbNetClass(object):
    def __init__(self, filename='', soup=None):
        self.soup = soup
        self.id = soup.attrs['ID']
        self.filename = filename
        self.frames = self.get_frames()
        self.themroles = self.get_themroles()
        self.members = self.get_members()
        self.predicates = self.get_predicates()
        self.args = self.get_args()
        self.examples = self.get_examples()
        # print("'" + self.id + "':" + ''.join([' ' for i in range(len("'" + self.id + "':"), 40)]) + str(self.class_args) + ",")

    def get_themroles(self):
        themroles = getattr(self, 'themroles', [])
        if not themroles:
            for themrole in self.soup.THEMROLES.find_all('THEMROLE'):
                role = utils.norm_role(themrole.attrs)
                selrestrs = themrole.find_all('SELRESTRS')

                themrole_ = VerbNetThemRole(role['type'], [])
                for selrestrs_ in selrestrs:
                    selres = VerbNetSelSynRestrs('sel', selrestrs_.attrs.get('logic', ''), [])
                    for selrestr in selrestrs_.find_all('SELRESTR'):
                        attrs = utils.norm(selrestr.attrs)
                        selres.restrs.append(VerbNetSelSynRestr('sel', attrs['type'], attrs['value']))

                    themrole_.restrs.append(selres)

                themroles.append(themrole_)

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
                members.append(VerbNetMember(member.attrs['name'][0],  # name
                                             self.id,  # vnclass
                                             self.filename,  # filename
                                             member.attrs['fnframe'],  # fnframe
                                             member.attrs['grouping'],  # grouping
                                             member.attrs['wn']))  # wn
        return members

    def get_member(self, lemma):
        for member in self.members:
            if member.name == lemma:
                return member
        return None

    def add_member(self, name, fnframe=[], grouping=[], wn=[]):
        self.members.append(VerbNetMember(name, self.id, self.filename, fnframe, grouping, wn))

    def get_examples(self):
        examples = getattr(self, 'examples', [])
        if not examples:
            for frame in self.frames:
                examples.append(frame.example)

        return examples

    def get_args(self, vnclass_args=[]):
        pred_args = []
        syntax_args = []
        themrole_args = [role.type for role in self.themroles]

        for frame in self.frames:
            pred_args.extend(frame.get_pred_args())
            syntax_args.append(frame.get_syntax_args())

        class_args = pred_args + syntax_args
        class_args = list(dict.fromkeys(Counter(utils.flatten(class_args))))

        if vnclass_args:
            class_args = list(dict.fromkeys(Counter(utils.flatten(vnclass_args + class_args))))

        # Consider the predicate equals to group arguments
        # for example equals(recipient, stimulus) means [recipient, stimulus]
        # inside the general argument structure of the class
        for pred in self.predicates:
            if pred.name == 'equals':
                group = []
                for arg in pred.args:
                    if arg.type != 'event' and arg.type != 'constant':
                        group.append(arg.value)

                remove = False
                for i, arg in enumerate(class_args):
                    if any([arg == group_arg for group_arg in group]):
                        if not remove:
                            class_args[i] = group
                            remove = True
                        else:
                            del class_args[i]

        slots = []
        for arg in class_args:
            slot = VerbNetArgSlot()
            if isinstance(arg, list):
                for a in arg:
                    slot.add_arg(a)
            else:
                slot.add_arg(arg)
            slots.append(slot)
        return slots

    def get_predicates(self):
        predicates = getattr(self, 'predicates', [])
        for frame in self.frames:
            for pred in frame.predicates:
                if not any([str(pred) == str(pr) for pr in predicates]):
                    predicates.append(pred)
        return predicates

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}id={self.id!r}{end}' \
               f'{indent_}filename={self.filename!r}{end}' \
               f'{indent_}args={self.args!r}{end}' \
               f'{"".join([arg.pprint(indent + 2, end) for arg in self.args])}' \
               f'{indent_}predicates={end}' \
               f'{"".join([pred.pprint(indent + 2, end) for pred in self.predicates])}' \
               f'{indent_}frames={end}' \
               f'{"".join([frame.pprint(indent + 2, end) for frame in self.frames])}' \
               f'{indent_}themroles={end}' \
               f'{"".join([role.pprint(indent + 2, end) for role in self.themroles])}' \
               f'{indent_}members={end}' \
               f'{"".join([member.pprint(indent + 2, end) for member in self.members])}'


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
        self.predicates = self.get_predicates()
        self.syntax_args = self.get_syntax_args()
        self.pred_args = self.get_pred_args()

    def get_syntax(self):
        syntax = getattr(self, 'syntax', [])
        if not syntax:
            for stx in self.soup.SYNTAX.find_all(['NP', 'VERB', 'PREP']):
                stx_tag = VerbNetSyntaxTag(stx.name,
                                           utils.norm_role(stx.attrs.get('value', '').replace('|', ' ').split()), [])

                for synrestr in stx.find_all('SYNRESTR'):
                    restr = utils.norm(synrestr.attrs)
                    stx_tag.restrs.append(VerbNetSelSynRestr('syn', restr['type'], restr['value']))

                for selrestr in stx.find_all('SELRESTR'):
                    restr = utils.norm(selrestr.attrs)
                    stx_tag.restrs.append(VerbNetSelSynRestr('sel', restr['type'], restr['value']))

                syntax.append(stx_tag)

        return syntax

    def get_syntax_args(self):
        syntax_args = getattr(self, 'syntax_args', [])
        if not syntax_args:
            for stx in self.syntax:
                if stx.type == 'NP':
                    syntax_args.append(stx.value[0])

        return syntax_args

    def get_pred_args(self):
        pred_args = getattr(self, 'pred_args', [])
        if not pred_args:
            for pred in self.predicates:
                pred_args.append(pred.get_role_args())

        return pred_args

    def get_predicates(self):
        preds = getattr(self, 'preds', [])
        if not preds:
            for pred in self.soup.SEMANTICS.find_all('PRED'):
                preds.append(VerbNetPredicate(pred))

        return preds

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}class_id={self.class_id!r}{end}' \
               f'{indent_}filename={self.filename!r}{end}' \
               f'{indent_}primary={self.primary!r}{end}' \
               f'{indent_}secondary={self.secondary!r}{end}' \
               f'{indent_}xtag={self.xtag!r}{end}' \
               f'{indent_}descr_num={self.descr_num!r}{end}' \
               f'{indent_}example={self.example!r}{end}' \
               f'{indent_}syntax={end}' \
               f'{"".join([stx.pprint(indent + 2, end) for stx in self.syntax])}' \
               f'{indent_}predicates={end}' \
               f'{"".join([pred.pprint(indent + 2, end) for pred in self.predicates])}'


class VerbNetPredicate(object):
    def __init__(self, soup=None):
        self.soup = soup
        self.bool = '' if 'bool' not in soup.attrs else soup.attrs['bool']
        self.name = soup.attrs['value']
        self.args = self.get_args()

    def add_arg(self, type, value, idx=-1):
        self.args.insert(idx, VerbNetArg(type, value))

    def get_args(self):
        args = getattr(self, 'args', [])
        if self.soup:
            if not args:
                for arg in self.soup.ARGS.find_all('ARG'):
                    # ** There is one case in admire-31.2.xml that a value appears as 'Stimulus, Attribute'
                    # in the predicate. I do not know if they will remove this in the future. The next
                    # piece of code is to be able to generalize to those kind of cases
                    for role in arg.attrs['value'].split(','):
                        args.append(VerbNetArg(utils.norm(arg.attrs['type']), utils.norm_role(role)))

        return args

    def get_role_args(self):
        role_args = []
        for arg in self.args:
            if arg.type != 'event' and arg.type != 'constant':
                role_args.append(arg.value)
        return role_args

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}bool={self.bool!r}{end}' \
               f'{indent_}name={self.name!r}{end}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint(indent + 2, end) for arg in self.args])}'

    def __str__(self):
        return f'{self.bool}{self.name}({",".join([str(arg.value) for arg in self.args])})'


class VerbNetSimplified(object):
    def __init__(self, vn, json_path=''):
        self.vn = vn
        self.json_path = json_path
        self.json = utils.fromjson(json_path)
        self.classes = self.get_classes()

    def get_classes(self):
        classes = getattr(self, 'classes', {})
        if not classes:
            if self.json:
                ...
            else:
                for cls_id, cls in self.vn.get_classes().items():
                    classes[cls_id] = VerbNetSimplifiedClass(cls)

        return classes

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}json_path={self.json_path!r}{end}' \
               f'{indent_}classes={end}' \
               f'{"".join([cls.pprint(indent + 2, end) for cls in self.classes.values()])}'


class VerbNetSimplifiedClass(object):
    def __init__(self, vnclass: VerbNetClass = None, json_class={}):
        self.json = json_class
        self.vnclass = vnclass
        self.id = vnclass.id
        self.args = self.get_args()
        self.predicates = self.get_predicates()
        self.members = self.get_members()
        self.examples = self.get_examples()

    def get_args(self):
        args = getattr(self, 'args', [])
        if not args:
            if self.json:
                ...
            elif self.vnclass:
                args = self.vnclass.get_args(vnclass_args.vnclass_dict[self.id])
        return args

    def get_predicates(self):
        predicates = getattr(self, 'predicates', [])
        if not predicates:
            if self.json:
                ...
            elif self.vnclass:
                predicates = self.vnclass.get_predicates()
        return predicates

    def get_members(self):
        members = getattr(self, 'examples', [])
        if not members:
            if self.json:
                ...
            elif self.vnclass:
                members = self.vnclass.get_members()
        return members

    def get_examples(self):
        examples = getattr(self, 'examples', [])
        if not examples:
            if self.json:
                ...
            elif self.vnclass:
                examples = self.vnclass.get_examples()
        return examples

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}id={self.id!r}{end}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint(indent + 2, end) for arg in self.args])}' \
               f'{indent_}predicates={end}' \
               f'{"".join([pred.pprint(indent + 2, end) for pred in self.predicates])}' \
               f'{indent_}members={end}' \
               f'{"".join([member.pprint(indent + 2, end) for member in self.members])}' \
               f'{indent_}examples={end}' \
               f'{"".join([indent_ + example + end for example in self.examples])}'


@dataclass
class VerbNetSelSynRestr:
    name: str
    type: str
    value: str

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}name={self.name!r}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}value={self.value!r}{end}'


@dataclass
class VerbNetSelSynRestrs:
    type: str
    logic: str
    restrs: List[VerbNetSelSynRestr] = field(default_factory=list)

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}logic={self.logic!r}{end}' \
               f'{indent_}restrs={end}' \
               f'{"".join([restr.pprint(indent + 2, end) for restr in self.restrs])}'


@dataclass
class VerbNetSyntaxTag:
    type: str
    value: list
    restrs: List[VerbNetSelSynRestr] = field(default_factory=list)

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}value={self.type!r}{end}' \
               f'{indent_}restrs={end}' \
               f'{"".join([restr.pprint(indent + 2, end) for restr in self.restrs])}'


@dataclass
class VerbNetThemRole:
    type: str
    restrs: List[VerbNetSelSynRestr] = field(default_factory=list)

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}restrs={end}' \
               f'{"".join([restr.pprint(indent + 2, end) for restr in self.restrs])}'


@dataclass
class VerbNetArg:
    type: str
    value: str

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}value={self.value!r}{end}'


@dataclass
class VerbNetArgSlot:
    value: list = field(default_factory=list)
    implicit: bool = False

    def add_arg(self, value):
        self.value.append(value)

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}value={self.value!r}{end}' \
               f'{indent_}implicit={self.implicit!r}{end}'


@dataclass
class VerbNetMember:
    name: str
    vnclass: str
    filename: str
    fnframe: list = field(default_factory=list)
    grouping: list = field(default_factory=list)
    wn: list = field(default_factory=list)

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}name={self.name!r}{end}' \
               f'{indent_}vnclass={self.vnclass!r}{end}' \
               f'{indent_}filename={self.filename!r}{end}' \
               f'{indent_}fnframe={self.fnframe!r}{end}' \
               f'{indent_}grouping={self.grouping!r}{end}' \
               f'{indent_}wn={self.wn!r}{end}'


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'corpora/verbnet/')
    vn = VerbNet(filename)
    vn_s = VerbNetSimplified(vn)
    print(vn_s.pprint())

    # verbs = vn.get_verbs()
