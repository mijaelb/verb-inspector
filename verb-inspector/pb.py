# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:51:58 2019

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


class PropBank(object):
    def __init__(self, path):
        self.path = Path(path)
        self.files_soup = self.parse()
        self.predicates = self.get_predicates()

    def parse(self):
        return utils.parse_xmls(self.path)

    def replace(self, str_, forstr_, lemma):
        utils.replace(str_, forstr_, self.path / self.predicates[lemma].filename)

    def get_predicates(self):
        predicates = getattr(self, 'predicates', {})
        if not predicates:
            for filename, soup in self.files_soup.items():
                for pred in soup.find_all('predicate'):
                    predicates[pred.attrs['lemma']] = PropBankPredicate(filename, pred)

        return predicates

    def get_lemmas(self):
        return self.predicates.keys()

    def get_rolesets(self, lemma):
        if lemma in self.predicates:
            return self.predicates[lemma].rolesets
        else:
            return None

    def get_roleset(self, roleset):
        tupl = re.match(r'(.+)\.(\d+)', roleset)
        if tupl:
            lemma, num = (tupl[1], tupl[2])
            predicate = self.predicates[lemma]
            for roleset_ in predicate.get_rolesets():
                if roleset_.id == roleset:
                    return roleset_
        return None

    def get_roles(self, roleset):
        roleset_ = self.get_roleset(roleset)
        if roleset_:
            roles = roleset_.get_roles()
            return roles
        return []

    def get_classes(self, roleset):
        roleset_ = self.get_roleset(roleset)
        if roleset_:
            classes = roleset_.get_classes()
            return classes
        return []

    def get_rolesets_from_class(self, lemma, cls_id):
        rolesets = self.get_rolesets(lemma)
        rls_ = []
        if rolesets:
            for roleset in rolesets:
                if any([class_ in cls_id for class_ in roleset.get_classes()]):
                    rls_.append(roleset)
        return rls_

    def get_rolesets_ids_from_class(self, lemma, cls_id):
        return [roleset.id for roleset in self.get_rolesets_from_class(lemma, cls_id)]

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}path={str(self.path)!r}{end}' \
               f'{indent_}predicates={end}' \
               f'{"".join([predicate.pprint(indent+2, end) for predicate in self.predicates.values()])}'


class PropBankPredicate(object):
    def __init__(self, filename, soup):
        self.soup = soup
        self.lemma = soup.attrs['lemma']
        self.filename = filename
        self.rolesets = self.get_rolesets()

    def get_rolesets(self):
        rolesets = getattr(self, 'rolesets', [])
        if not rolesets:
            for roleset in self.soup.find_all('roleset'):
                rolesets.append(PropBankRoleset(self.filename, roleset))
        return rolesets

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}lemma={self.lemma!r}{end}' \
               f'{indent_}filename={self.filename!r}{end}' \
               f'{indent_}rolesets={end}' \
               f'{"".join([roleset.pprint(indent+2, end) for roleset in self.rolesets])}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(lemma={self.lemma!r}, filename={self.filename!r}, rolesets={self.rolesets!r}')


class PropBankRoleset(object):
    def __init__(self, filename, soup):
        self.soup = soup
        self.filename = filename
        self.id = soup.attrs['id']
        self.name = soup.attrs['name']
        self.aliases = self.get_aliases()
        self.roles = self.get_roles()
        self.examples = self.get_examples()

    def get_aliases(self):
        aliases = getattr(self, 'aliases', [])
        if not aliases:
            for alias in self.soup.aliases.find_all('alias'):
                pb_alias = PropBankAlias()
                pb_alias.fill(alias.attrs, alias.text)
                aliases.append(pb_alias)

        return aliases

    def get_roles(self):
        roles = getattr(self, 'roles', [])
        if not roles:
            for role in self.soup.roles.find_all('role'):
                pb_role = PropBankRole()
                pb_role.fill(utils.norm(role.attrs))
                for vnrole in role.find_all('vnrole'):
                    pb_role.add_vnrole(utils.norm_role(vnrole.attrs['vntheta']), (vnrole['vncls']))
                roles.append(pb_role)
        return roles

    def get_examples(self):
        examples = getattr(self, 'examples', [])
        if not examples:
            for example in self.soup.find_all('example'):
                pb_example = PropBankExample()
                text = example.find_all('text')[0].text if example.find_all('text') else ''
                pb_example.fill(example.attrs, text)

                if example.inflection:
                    pb_example.inflection.fill(example.inflection.attrs)

                for arg in example.find_all(['arg', 'rel']):
                    pb_example.add_arg(arg.name, arg.get('f', ''), arg.get('n', ''), arg.text)
                examples.append(pb_example)
        return examples

    def get_classes(self):
        classes = []
        for role in self.roles:
            for vnrole in role.vnroles:
                classes.append(vnrole.vncls)

        return list(dict.fromkeys(classes))

    def get_fn(self, pos='v'):
        fn = []
        for alias in self.aliases:
            if alias.pos == pos:
                fn.extend(alias.framenet)
        return fn

    def get_examples_text(self):
        return [example.text for example in self.examples]

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent+1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}id={self.id!r}{end}' \
               f'{indent_}name={self.name!r}{end}' \
               f'{indent_}filename={self.filename!r}{end}' \
               f'{indent_}aliases={end}' \
               f'{"".join([alias.pprint(indent+2, end) for alias in self.aliases])}' \
               f'{indent_}roles={end}' \
               f'{"".join([roles.pprint(indent+2 , end) for roles in self.roles])}' \
               f'{indent_}examples={end}' \
               f'{"".join([exampl.pprint(indent+2, end) for exampl in self.examples])}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(id={self.id!r}, name={self.name!r}, filename={self.filename!r}, aliases={self.aliases!r}, roles={self.roles!r}, examples={self.examples!r})')

    def __str__(self):
        return str(self.id)


@dataclass
class PropBankInflection:
    aspect: str = ''
    form: str = ''
    person: str = ''
    tense: str = ''
    voice: str = ''

    def fill(self, attrs):
        self.aspect = attrs.get('aspect', '')
        self.form = attrs.get('form', '')
        self.person = attrs.get('person', '')
        self.tense = attrs.get('tense', '')
        self.voice = attrs.get('voice', '')

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}aspect={self.aspect!r}{end}' \
               f'{indent_}form={self.form!r}{end}' \
               f'{indent_}person={self.person!r}{end}' \
               f'{indent_}tense={self.tense!r}{end}' \
               f'{indent_}voice={self.voice!r}{end}'


@dataclass
class PropBankExampleArg:
    type: str
    f: str
    n: str
    text: str

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}f={self.f!r}{end}' \
               f'{indent_}n={self.n!r}{end}' \
               f'{indent_}text={self.text!r}{end}'

@dataclass
class PropBankExample:
    name: str = ''
    src: str = ''
    type: str = ''
    text: str = ''
    inflection: PropBankInflection = PropBankInflection()
    args: List[PropBankExampleArg] = field(default_factory=list)

    def add_arg(self, type, f, n, text):
        self.args.append(PropBankExampleArg(type, f, n, text))

    def fill(self, attrs, text):
        self.name = attrs.get('name', '')
        self.src = attrs.get('src', '')
        self.type = attrs.get('type', '')
        self.text = text

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}name={self.name!r}{end}' \
               f'{indent_}src={self.src!r}{end}' \
               f'{indent_}type={self.type!r}{end}' \
               f'{indent_}text={self.text!r}{end}' \
               f'{indent_}inflection={end}' \
               f'{self.inflection.pprint(indent+1, end)}' \
               f'{indent_}args={end}' \
               f'{"".join([arg.pprint(indent+2, end) for arg in self.args])}'


@dataclass
class PropBankAlias:
    framenet: str = field(default_factory=list)
    pos: str = ''
    verbnet: str = field(default_factory=list)
    word: str = field(default_factory=list)

    def fill(self, attrs, word):
        self.framenet = attrs.get('framenet', '').split()
        self.pos = attrs.get('pos', '')
        self.verbnet = attrs.get('verbnet', '').split()
        self.word = word.split()

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}framenet={self.framenet!r}{end}' \
               f'{indent_}pos={self.pos!r}{end}' \
               f'{indent_}verbnet={self.verbnet!r}{end}' \
               f'{indent_}word={self.word!r}{end}'


@dataclass
class PropBankVNRole:
    vntheta: str
    vncls: str

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}vntheta={self.vntheta!r}{end}' \
               f'{indent_}vncls={self.vncls!r}{end}'


@dataclass
class PropBankRole:
    descr: str = ''
    f: str = ''
    n: str = ''
    vnroles: List[PropBankVNRole] = field(default_factory=list)

    def add_vnrole(self, vntheta, vncls):
        self.vnroles.append(PropBankVNRole(vntheta, vncls))

    def fill(self, attrs):
        self.descr = attrs.get('descr', '')
        self.f = attrs.get('f', '')
        self.n = attrs.get('n', '')

    def pprint(self, indent=0, end='\n'):
        indent_in = utils.indent(indent)
        indent_ = utils.indent(indent + 1)
        return f'{indent_in}{self.__class__.__name__}{end}' \
               f'{indent_}descr={self.descr!r}{end}' \
               f'{indent_}f={self.f!r}{end}' \
               f'{indent_}n={self.n!r}{end}' \
               f'{"".join([vnrole.pprint(indent + 1, end) for vnrole in self.vnroles])}'


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'corpora/propbank/frames/')
    propbank = PropBank(filename)
