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

    def get_inventories(self):
        inventories = getattr(self, 'inventories', [])
        if not inventories:
            for filename, soup in self.files_soup.items():
                if soup.inventory:
                    inventories.append(GroupingInventory(filename, soup.inventory))

        return inventories


class GroupingInventory(object):
    def __init__(self, filename, soup):
        tupl = re.match(r'(.+)(-\w)', soup.attrs['lemma'])
        self.lemma, self.type = (tupl[1], tupl[2])
        self.filename = filename
        self.soup = soup
        self.senses = self.get_senses()

    def get_senses(self):
        senses = getattr(self, 'senses', [])
        if not senses:
            for sense in self.soup.find_all('sense'):
                senses.append(GroupingSense(self.filename, sense))
        return senses


class GroupingSense(object):
    def __init__(self, filename, soup):
        self.soup = soup
        self.group = soup.attrs.get('group', '')
        self.n = soup.attrs.get('n', '')
        self.name = soup.attrs.get('name', '')
        self.type = soup.attrs.get('type', '')
        self.filename = filename
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
                        mappings[mapping.name].append(values)

        return mappings


if __name__ == '__main__':
    grouping = Groupings('corpora/ontonotes/sense-inventories/')
