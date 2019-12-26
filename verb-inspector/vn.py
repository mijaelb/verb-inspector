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


class VerbNetBase(object):
    def __init__(self):
        self.classes = {}

    def get_classes(self, lemma='', class_ids=[]):
        classes = getattr(self, 'classes', {})
        if classes:
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

    def get_complete_class_id(self, id):
        for class_id in self.classes:
            tupl = re.match(r'(\w+)-(.*)', class_id)
            if tupl:
                if tupl[2] == id:
                    return class_id
        return id

    def get_complete_classes_ids(self, classes_ids):
        class_ids = []
        for cls in classes_ids:
            class_ids.append(self.get_complete_class_id(cls))

        return class_ids

    def get_classes_from_grouping(self, lemma, sense_id):
        classes = {}
        for cls, obj in self.classes.items():
            for member in obj.members:
                if sense_id in member.grouping:
                    classes[cls] = obj

        return classes

    def get_classes_ids_from_grouping(self, lemma, sense_id):
        return [cls for cls in self.get_classes_from_grouping(lemma, sense_id)]

    def get_fn_from_classes(self, lemma, classes):
        fn = []
        if classes:
            for class_id in classes:
                cls = self.get_class(class_id)
                try:
                    member = cls.get_member(lemma)
                    if member:
                        fn.extend(member.fnframe)
                except:
                    print(f'get_fn_from_class({lemma},{class_id}) not found!')

        return list(dict.fromkeys(fn))

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

    def get_all_predicates_name(self):
        predicates = []
        for cls in self.classes.values():
            for pred in cls.predicates:
                if not any([str(pred.name) == str(pr) for pr in predicates]):
                    predicates.append(pred.name)
        return predicates

    def replace_predicate_name(self, current, new):
        for cls in self.classes.values():
            for pred in cls.predicates:
                if pred.name == current:
                    pred.name = new

    def get_classes_by_predicate(self, pred_name):
        classes = {}
        for cls in self.classes.values():
            for pred in cls.predicates:
                if pred.name == pred_name and cls.id not in classes:
                    classes[cls.id] = cls

        return classes

    def get_predicates_from_class(self, class_id):
        cls = self.get_class(class_id)
        if cls:
            return cls.get_predicates()

        return []

    def change_class_name(self, class_id, new_id):
        cls = self.get_class(class_id)
        if cls:
            cls.id = new_id
            cls.change_class_name(class_id, new_id)
            self.classes = {key if key != class_id else new_id: cls_ for key, cls_ in self.classes.items()}
            return True

        return False

    def __str__(self):
        return str(self.classes.keys())

    def __iter__(self):
        for class_id, cls in self.classes.items():
            yield class_id, dict(cls)


class VerbNet(VerbNetBase):
    def __init__(self, path=''):
        self.path = Path(path)
        self.files_soup = self.parse()
        self.classes = self.load_classes()
        self.lemmas = self.get_lemmas()

    def parse(self):
        return utils.parse_xmls(self.path, 'lxml-xml')

    def replace(self, str_, forstr_, class_id):
        utils.replace(str_, forstr_, self.path / self.classes[class_id].filename)

    def load_classes(self):
        ''' Extract every VNCLASS and VNSUBCLASS into a VerbClass object '''
        classes = getattr(self, 'classes', {})
        if not classes:
            for filename, soup in self.files_soup.items():
                classes[soup.VNCLASS.attrs['ID']] = VerbNetClass(filename, soup.VNCLASS)
                for vnsubclass in soup.find_all('VNSUBCLASS'):
                    classes[vnsubclass.attrs['ID']] = VerbNetClass(filename, vnsubclass)
        return classes

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}path={self.path!r}{end}' \
               f'{indent_}classes={end}' \
               f'{"".join([cls.pprint(indent + 2, end) for cls in self.classes.values()])}'


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
                member.attrs['name'] = member.attrs['name'][0]
                mem = VerbNetMember()
                mem.fill_dict(member.attrs)
                mem.id = self.id
                mem.filename = self.filename
                members.append(mem)
        return members

    def get_member(self, lemma):
        for member in self.members:
            if member.name == lemma:
                return member
        return None

    def add_member(self, name, fnframe=None, grouping=None, wn=None):
        fnframe = [] if not fnframe else utils.norm(fnframe)
        grouping = [] if not grouping else utils.norm(grouping, False)
        wn = [] if not wn else wn
        self.members.append(VerbNetMember(name, self.id, self.filename, fnframe, grouping, wn))

    def get_examples(self):
        examples = getattr(self, 'examples', [])
        if not examples:
            for frame in self.frames:
                examples.append(frame.example)

        return examples

    def get_args(self, vnclass_args=None):
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
                            class_args.pop(i)

        args = []
        for i, arg in enumerate(class_args):
            if isinstance(arg, list):
                for a in arg:
                    args.append(VerbNetArg('', a, self.id, i, False))
            else:
                args.append(VerbNetArg('', arg, self.id, i, False))
        return args

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

    def __iter__(self):
        yield 'id', self.id
        yield 'filename', self.filename
        yield 'args', [dict(arg) for arg in self.args]
        yield 'predicates', [dict(pred) for pred in self.predicates]
        yield 'frame', [dict(frame) for frame in self.frames]
        yield 'role', [dict(role) for role in self.themroles]
        yield 'member', [dict(member) for member in self.members]


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
        predicates = getattr(self, 'preds', [])
        if not predicates:
            for pred in self.soup.SEMANTICS.find_all('PRED'):
                predicate = VerbNetPredicate()
                predicate.fill_soup(pred)
                predicates.append(predicate)

        return predicates

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

    def __iter__(self):
        yield 'class_id', self.class_id
        yield 'filename', self.filename
        yield 'primary', self.primary
        yield 'secondary', self.secondary
        yield 'xtag', self.xtag
        yield 'descr_num', self.descr_num
        yield 'example', self.example
        yield 'syntax', [dict(stx) for stx in self.syntax]
        yield 'predicates', [dict(pred) for pred in self.predicates]


@dataclass
class VerbNetArg:
    type: str = ''
    value: str = ''
    cls: str = ''
    slot: int = -1
    implicit: bool = False
    implicit_values: list = field(default_factory=list)

    def fill_dict(self, dict):
        self.type = dict.get('type', '')
        self.value = dict.get('value', '')
        self.cls = dict.get('cls', '')
        self.slot = dict.get('slot', -1)
        self.implicit = bool(dict.get('implicit', 'false'))

    def change_class_name(self, class_id, new_id):
        if self.cls == class_id:
            self.cls = new_id

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}value={self.value!r}{end}' \
               f'{indent_}cls={self.cls!r}{end}' \
               f'{indent_}slot={self.slot!r}{end}' \
               f'{indent_}implicit={self.implicit!r}{end}'

    def verb_dict(self):
        return {'value': self.value, 'cls': self.cls, 'slot': self.slot, 'implicit': self.implicit}

    def general_dict(self):
        return {'value': self.value, 'slot': self.slot, 'implicit': self.implicit}

    def pred_dict(self):
        return {'type': self.type, 'value': self.value}

    def __iter__(self):
        yield 'type', self.type
        yield 'value', self.value
        yield 'cls', self.cls
        yield 'slot', self.slot
        yield 'implicit', self.implicit

    def __str__(self):
        return f'{self.type}: {self.value}'


@dataclass
class VerbNetPredicate(object):
    bool: str = ''
    name: str = ''
    args: List[VerbNetArg] = field(default_factory=list)

    def add_arg(self, type, value):
        self.args.append(VerbNetArg(type, value))

    def edit_args_name(self, arr):
        if len(arr) < len(self.args):
            for i in range(len(arr) - 1, len(self.args) - 1):
                self.args.pop(i)

        if arr:
            for i, arg in enumerate(arr):
                if arg != '':
                    arg = ''.join(arg.split()[0])

                if i > len(self.args) - 1:
                    if re.match(r'e+(\d+)', arg):
                        self.add_arg('event', arg)
                    else:
                        self.add_arg('themrole', arg)
                else:
                    if re.match(r'e+(\d+)', arg):
                        self.args[i].type = 'event'
                    self.args[i].value = arg

    def fill_soup(self, soup):
        self.bool = '' if 'bool' not in soup.attrs else soup.attrs['bool']
        self.name = ''.join(soup.attrs['value'].split()).lower()
        self.args = []
        for arg in soup.ARGS.find_all('ARG'):
            # ** There is one case in admire-31.2.xml that a value appears as 'Stimulus, Attribute'
            # in the predicate. I do not know if they will remove this in the future. The next
            # piece of code is to be able to generalize to those kind of cases
            for role in arg.attrs['value'].split(','):
                self.args.append(VerbNetArg(utils.norm(arg.attrs['type']), utils.norm_role(role)))

    def fill_dict(self, dict):
        self.bool = dict.get('bool', '')
        self.name = ''.join(dict.get('name', '').split()).lower()
        self.args = []
        for arg in dict.get('args', []):
            self.args.append(VerbNetArg(utils.norm(arg['type']), utils.norm_role(arg['value'])))

    def get_role_args(self):
        role_args = []
        for arg in self.args:
            if arg.type != 'event' and arg.type != 'constant':
                role_args.append(arg.value)
        return role_args

    def change_class_name(self, class_id, new_id):
        for arg in self.args:
            arg.change_class_name(class_id, new_id)

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}bool={self.bool!r}{end}' \
               f'{indent_}name={self.name!r}{end}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint(indent + 2, end) for arg in self.args])}'

    def __iter__(self):
        yield 'bool', self.bool
        yield 'name', self.name
        yield 'args', [arg.pred_dict() for arg in self.args]

    def __str__(self):
        return f'{self.bool}{self.name}({", ".join([str(arg.value) for arg in self.args])})'


class VerbNetSimplified(VerbNetBase):
    def __init__(self, corpus_path='', json_path=''):
        self.vn = VerbNet(corpus_path)
        self.json_path = json_path
        self.json = utils.fromjson(self.json_path)
        self.classes = self.load_classes()
        self.lemmas = self.get_lemmas()

    def load(self, filename=''):
        if filename:
            json_path = filename
            json = utils.fromjson(filename)
        elif self.json_path:
            json_path = self.json_path
            json = utils.fromjson(self.json_path)

        if json:
            self.json = json
            self.json_path = json_path
            self.classes = self.load_classes()

    def save(self, filename=''):
        if filename:
            utils.tojson(filename, dict(self))
        elif self.json_path:
            utils.tojson(self.json_path, dict(self))

    def load_classes(self):
        classes = {}
        if self.json:
            classes = {class_id: VerbNetSimplifiedClass(self.vn.classes[class_id], cls)
                       for class_id, cls in self.json.items()}
        else:
            classes = {class_id: VerbNetSimplifiedClass(cls)
                       for class_id, cls in self.vn.get_classes().items()}
        return classes

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}json_path={self.json_path!r}{end}' \
               f'{indent_}classes={end}' \
               f'{"".join([cls.pprint(indent + 2, end) for cls in self.classes.values()])}'

    def __iter__(self):
        for class_id, cls in self.classes.items():
            yield class_id, dict(cls)


class VerbNetSimplifiedClass(object):
    def __init__(self, vnclass: VerbNetClass = None, json_class={}):
        self.vnclass = vnclass
        self.json = json_class
        self.id = self.json['id'] if self.json else self.vnclass.id
        self.args = self.get_args()
        self.predicates = self.get_predicates()
        self.members = self.get_members()
        self.examples = self.get_examples()

    def change_class_name(self, class_id, new_id):
        for arg in self.args:
            arg.change_class_name(class_id, new_id)

        for pred in self.predicates:
            pred.change_class_name(class_id, new_id)

    def add_pred(self, bool='', name='', args=None):
        args = [] if args is None else args
        self.predicates.append(VerbNetPredicate(bool, name, args))

    def add_arg(self, value='empty', cls='', slot=0, implicit=False):
        i = -1
        for i, arg in enumerate(self.args):
            if arg.slot > slot:
                break

        self.args.insert(i + 1, VerbNetArg('', value, cls, slot, implicit))

    def remove_arg(self, arg):
        for i, arg_ in enumerate(self.args):
            if arg == arg_:
                return self.args.pop(i)

    def get_args(self):
        args = getattr(self, 'args', [])
        if not args:
            if self.json:
                for arg_dict in self.json['args']:
                    arg = VerbNetArg()
                    arg.fill_dict(arg_dict)
                    arg.cls = self.id
                    args.append(arg)
            elif self.vnclass:
                args = self.vnclass.get_args(vnclass_args.vnclass_dict[self.id])
        return args

    def get_predicates(self):
        predicates = getattr(self, 'predicates', [])
        if not predicates:
            if self.json:
                for pred_dict in self.json['predicates']:
                    predicate = VerbNetPredicate()
                    predicate.fill_dict(pred_dict)
                    predicates.append(predicate)
            elif self.vnclass:
                predicates = self.vnclass.get_predicates()

        return predicates

    def get_members(self):
        members = getattr(self, 'examples', [])
        if not members:
            if self.json:
                for mem in self.json['members']:
                    member = VerbNetMember()
                    member.fill_dict(mem)
                    members.append(member)
            elif self.vnclass:
                members = self.vnclass.get_members()
        return members

    def get_member(self, lemma):
        for member in self.members:
            if member.name == lemma:
                return member
        return None

    def get_examples(self):
        examples = getattr(self, 'examples', [])
        if not examples:
            if self.json:
                for ie in self.json['examples']:
                    examples.append(ie)
            elif self.vnclass:
                examples = self.vnclass.get_examples()
        return examples

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

    def __iter__(self):
        yield 'id', self.id
        yield 'args', [arg.general_dict() for arg in self.args]
        yield 'predicates', [dict(pred) for pred in self.predicates]
        yield 'members', [dict(member) for member in self.members]
        yield 'examples', self.examples


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

    def __iter__(self):
        yield 'name', self.name
        yield 'type', self.type
        yield 'value', self.value


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

    def __iter__(self):
        yield 'type', self.type
        yield 'logic', self.logic
        yield 'restrs', [dict(restr) for restr in self.restrs]


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

    def __iter__(self):
        yield 'type', self.type
        yield 'value', self.value
        yield 'restrs', [dict(restr) for restr in self.restrs]


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

    def __iter__(self):
        yield 'type', self.type
        yield 'restrs', [dict(restr) for restr in self.restrs]


@dataclass
class VerbNetMember:
    name: str = ''
    vnclass: str = ''
    filename: str = ''
    fnframe: list = field(default_factory=list)
    grouping: list = field(default_factory=list)
    wn: list = field(default_factory=list)

    def fill_dict(self, dict):
        self.name = utils.norm(dict.get('name', self.name))
        self.vnclass = dict.get('vnclass', self.vnclass)
        self.filename = dict.get('filename', self.filename)
        self.fnframe = utils.norm(dict.get('fnframe', self.fnframe))
        self.grouping = utils.norm(dict.get('grouping', self.grouping), False)
        self.wn = dict.get('wn', self.wn)

    def get_fn(self):
        return self.fnframe

    def get_gr(self):
        return self.grouping

    def get_wn(self):
        return self.wn

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

    def __iter__(self):
        yield 'name', self.name
        yield 'fnframe', self.fnframe
        yield 'grouping', self.grouping
        yield 'wn', self.wn


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'corpora/verbnet/')
    json = os.path.join(dirname, 'data/verbnet_simplified.json')
    vn_s = VerbNetSimplified(filename, json)
    print(vn_s.pprint())
    print(dict(vn_s)['work-73.2'])

    vn_s.save(json)

    # verbs = vn.get_verbs()
