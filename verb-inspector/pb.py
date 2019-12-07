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


class PropBank(object):
    def __init__(self, path):
        self.path = Path(path)
        self.files_soup = self.parse()
        self.predicates = self.get_predicates()

    def parse(self):
        return utils.parse_xmls(self.path)

    def get_predicates(self):
        predicates = getattr(self, 'predicates', {})
        if not predicates:
            for filename, soup in self.files_soup.items():
                for pred in soup.find_all('predicate'):
                    predicates[pred.attrs['lemma']] = PropBankPredicate(filename, pred)

        return predicates


class PropBankPredicate(object):
    def __init__(self, filename, soup):
        self.lemma = soup.attrs['lemma']
        self.soup = soup
        self.filename = filename
        self.rolesets = self.get_rolesets()
        self.dict = {'lemma': self.lemma,
                     'rolesets': [str(roleset) for roleset in self.rolesets],
                     'filename': self.filename}

    def get_rolesets(self):
        rolesets = getattr(self, 'rolesets', [])
        if not rolesets:
            for roleset in self.soup.find_all('roleset'):
                rolesets.append(PropBankRoleset(self.filename, roleset))
        return rolesets

    def __str__(self):
        return str(self.dict)


class PropBankRoleset(object):
    def __init__(self, filename, soup):
        self.id = soup.attrs['id']
        self.name = soup.attrs['name']
        self.soup = soup
        self.filename = filename
        self.aliases = self.get_aliases()
        self.roles = self.get_roles()
        self.examples = self.get_examples()

    def get_aliases(self):
        aliases = getattr(self, 'aliases', [])
        if not aliases:
            for alias in self.soup.aliases.find_all('alias'):
                al = alias.attrs
                al['text'] = alias.text
                aliases.append(al)

        return aliases

    def get_roles(self):
        roles = getattr(self, 'roles', [])
        if not roles:
            for role in self.soup.roles.find_all('role'):
                role_dict = utils.norm(role.attrs)
                role_dict['vnroles'] = []
                for vnrole in self.soup.roles.find_all('vnrole'):
                    vnrole.attrs['vntheta'] = utils.norm_role(vnrole.attrs['vntheta'])
                    role_dict['vnroles'].append(vnrole.attrs)
                roles.append(role_dict)
        return roles

    def get_examples(self):
        examples = getattr(self, 'examples', [])
        if not examples:
            for example in self.soup.find_all('example'):
                exa = example.attrs
                exa['inflection'] = example.inflection.attrs if example.inflection else {}
                exa['text'] = example.find_all('text')[0].text if example.find_all('text') else ''
                exa['args'] = []
                for arg in example.find_all(['arg', 'rel']):
                    arg_ = {}
                    arg_['tag'] = arg.name
                    arg_.update(arg.attrs)
                    arg_['text'] = arg.text
                    exa['args'].append(arg_)
                examples.append(exa)
        return examples

    def __str__(self):
        return self.id


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'corpora/propbank/frames/')
    propbank = PropBank(filename)
