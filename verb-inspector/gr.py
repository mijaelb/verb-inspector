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
            inventories = list(filter(lambda x: x.type == type, inventories))

        return inventories

    def get_inventory(self, lemma, type='v'):
        return self.inventories[lemma+'-'+type]

    def get_sense(self, sense_id, type='v'):
        lemma = sense_id.split('.')[0]
        inventory = self.get_inventory(lemma, type)
        return inventory.get_sense(sense_id)

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

    def __str__(self):
        return self.lemma


class GroupingSense(object):
    def __init__(self, lemma, filename, soup):
        self.filename = filename
        self.lemma = lemma
        self.soup = soup
        self.group = soup.attrs.get('group', '')
        self.n = soup.attrs.get('n', '')
        self.name = soup.attrs.get('name', '')
        self.type = soup.attrs.get('type', '')
        self.id = self.lemma + '.' + ('0' + self.n if len(self.n) < 2 else self.n)
        self.examples = self.get_examples()
        self.mappings = self.get_mappings()

    def get_examples(self):
        examples = getattr(self, 'examples', [])
        if not examples and self.soup.examples:
            examples = [' '.join(ie.split()) for ie in self.soup.examples.text.strip().split('\n')]
        return examples

    def get_mappings(self):
        mappings = getattr(self, 'mappings', {})
        if not mappings:
            mappings = {'wn': [], 'vn': [], 'pb': [], 'fn': [], 'gr_sense': []}
            for mapping in self.soup.mappings.find_all(list(mappings.keys())):
                values = ' '.join(mapping.text.strip().split(',')).split()
                if values and values[0].lower() not in ['nm', 'np']:
                    if mapping.name == 'wn':
                        lemma = mapping.attrs.get('lemma', '')
                        version = mapping.attrs.get('version', '')
                        mappings['wn'].append({'lemma': lemma, 'version': version, 'values': values})
                    else:
                        mappings[mapping.name] = values

        return mappings

    def get_wordnet_mappings(self):
        return self.mappings['wn']

    def get_verbnet_mappings(self):
        return self.mappings['vn']

    def get_propbank_mappings(self):
        return self.mappings['pb']

    def get_framenet_mappings(self):
        return self.mappings['fn']

    def __str__(self):
        return self.id

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'corpora/ontonotes/sense-inventories/')
    grouping = Groupings(filename)
    print(grouping.get_inventories('v'))
