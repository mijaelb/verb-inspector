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


class Groupings(object):
    def __init__(self, path):
        self.path = Path(path)
        self.files_soup = self.parse()
        self.inventories = self.get_inventories()

    def parse(self):
        return utils.parse_xmls(self.path)

    def get_inventories(self, type=''):
        inventories = getattr(self, 'inventories', {})
        if not inventories:
            for filename, soup in self.files_soup.items():
                if soup.inventory:
                    inventories[soup.inventory.attrs['lemma']] = GroupingInventory(filename, soup.inventory)
        if type:
            inventories = {key: inventories[key] for key in inventories if inventories[key].type == type}

        return inventories

    def get_inventory(self, lemma, type='v'):
        if lemma in self.inventories:
            return self.inventories[lemma + '-' + type]
        return None

    def get_sense(self, sense_id, type='v'):
        lemma = sense_id.split('.')[0]
        inventory = self.get_inventory(lemma, type)
        return inventory.get_sense(sense_id)

    def get_lemmas(self, type='v'):
        return [d.lemma for key, d in self.get_inventories(type).items()]

    def get_senses(self, lemma, type='v'):
        return self.inventories[lemma + '-' + type].senses

    def get_pb_ids(self, lemma, type='v'):
        senses = self.get_senses(lemma, type)
        pb_ids = []
        for sense in senses.values():
            pb_ids += sense.mappings.pb

        return list(dict.fromkeys(pb_ids))

    def get_senses_from_pb(self, lemma, roleset, type='v'):
        gr = []
        inv = self.get_inventory(lemma)
        if inv:
            for sense in inv.senses:
                if roleset in sense.mappings.pb:
                    gr.append(sense)
        return gr

    def get_vn_classes(self, lemma, type='v'):
        senses = self.get_senses(lemma, type)
        vn_classes = []
        for sense in senses.values():
            vn_classes += sense.mappings.vn
        return list(dict.fromkeys(vn_classes))


class GroupingInventory(object):
    def __init__(self, filename, soup):
        tupl = re.match(r'(.+)-(\w)', soup.attrs['lemma'])
        self.lemma, self.type = (tupl[1], tupl[2])
        self.filename = filename
        self.soup = soup
        self.senses = self.get_senses()

    def get_senses(self):
        senses = getattr(self, 'senses', {})
        if not senses:
            for sense in self.soup.find_all('sense'):
                sense_obj = GroupingSense(self.lemma, self.filename, sense)
                senses[sense_obj.id] = sense_obj
        return senses

    def get_sense(self, sense_id):
        if sense_id in self.senses:
            return self.senses[sense_id]

        for sense in self.senses.values():
            if sense_id == sense.n or sense_id == sense.id:
                return sense

        return None

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'lemma={self.lemma!r}, '
                f'filename={self.filename!r}, '
                f'senses={self.senses!r}) ')

    def __str__(self):
        return self.lemma


class GroupingSense(object):
    def __init__(self, lemma, filename, soup):
        self.soup = soup
        self.n = soup.attrs.get('n', '')
        self.lemma = lemma
        self.id = self.lemma + '.' + ('0' + self.n if len(self.n) < 2 else self.n)
        self.name = soup.attrs.get('name', '')
        self.filename = filename
        self.mappings = self.get_mappings()
        self.group = soup.attrs.get('group', '')
        self.type = soup.attrs.get('type', '')
        self.examples = self.get_examples()

    def get_examples(self):
        examples = getattr(self, 'examples', [])
        if not examples and self.soup.examples:
            examples = [' '.join(ie.split()) for ie in self.soup.examples.text.strip().split('\n')]
        return examples

    def get_mappings(self):
        mappings = getattr(self, 'mappings', None)
        if not mappings:
            mappings = GroupingMappings()
            for mapping in self.soup.mappings.find_all(['wn', 'vn', 'pb', 'fn', 'gr_sense']):
                values = ' '.join(mapping.text.strip().split(',')).split()
                if values and values[0].lower() not in ['nm', 'np', 'nn']:
                    if mapping.name == 'wn':
                        mappings.add_wn(mapping.attrs.get('lemma', ''),
                                        mapping.attrs.get('version', ''),
                                        values)
                    else:
                        mappings.fill(mapping.name, values)

        return mappings

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'lemma={self.lemma!r}, '
                f'id={self.id!r}, '
                f'name={self.name!r}, '
                f'filename={self.filename!r}, '
                f'mappings={self.mappings!r}, '
                f'group={self.group!r},'
                f'type={self.type!r}, '
                f'n={self.n!r}, '
                f'examples={self.examples!r})')

    def __str__(self):
        return self.id


@dataclass
class WordNetRef:
    lemma: str
    version: str
    values: list


@dataclass
class GroupingMappings:
    gr_sense: list = field(default_factory=list)
    wn: List[WordNetRef] = field(default_factory=list)
    pb: list = field(default_factory=list)
    vn: list = field(default_factory=list)
    fn: list = field(default_factory=list)

    def add_wn(self, lemma, version, values):
        values = [value.lower() for value in values]
        self.wn.append(WordNetRef(lemma.lower(), version, values))

    def fill(self, mapping_name, values):
        values = [value.lower() for value in values]
        if mapping_name == 'pb':
            self.pb = values
        elif mapping_name == 'vn':
            self.vn = values
        elif mapping_name == 'fn':
            self.fn = values
        elif mapping_name == 'gr_sense':
            self.gr_sense = values


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'corpora/ontonotes/sense-inventories/')
    grouping = Groupings(filename)
    print(grouping.get_inventories('v'))
