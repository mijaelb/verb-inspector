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
sys.path.append("utils/")

import utils

class Groupings(object):
    def __init__(self, path):

        self.path = Path(path)
        self.files_soup = self.parse()
        self.inventories = self.get_inventories()
        ...

    def parse(self):
        return utils.parse_xmls(self.path)

    def get_inventories(self):
        inventories = getattr(self, 'inventories', [])
        if not inventories:
            for fname, soup in self.files_soup.items():
                inv = soup.inventory
                if not inv:
                    print(fname)
                else:
                    inventories.append(Inventory(inv.attrs['lemma'], fname, soup))

        return inventories

    def get_senses(self):
        senses = getattr(self, 'senses', [])
        #if not senses:
            #for sense in enumerate(self.soup.FRAMES.find_all('FRAME'):
                #frames.append(VerbFrame(self.id, frame))


class Inventory(object):
    def __init__(self, lemma_type, fname, soup):
        tupl = re.match(r'(.+)(-\w)', lemma_type)
        self.lemma, self.type = (tupl[1], tupl[2])
        self.fname = fname
        self.soup = soup
        self.senses = self.get_senses()
        #print(fname)

    def get_senses(self):
        senses = getattr(self, 'senses', [])
        if not senses:
            for sense in self.soup.find_all('sense'):
                senses.append(Sense(sense.attrs, self.fname, sense))
        return senses


class Sense(object):
    def __init__(self, attrs, fname, soup):
        self.group = attrs.get('group', '')
        self.n = attrs.get('n', '')
        self.name = attrs.get('name', '')
        self.type = attrs.get('type', '')
        self.fname = fname
        self.soup = soup
        self.mappings = self.get_mappings()
        #print(' '.join([self.group, self.n, self.name, self.type]))

    def get_examples(self):
        examples = getattr(self, 'examples', [])

        return examples

    def get_mappings(self):
        mappings = getattr(self, 'mappings', {})
        if not mappings:
            mappings = {'wn': [], 'vn': [], 'pb': [], 'fn': [], 'gr_sense': []}
            print(self.fname)
            for mapping in self.soup.mappings.find_all(list(mappings.keys())):
                values = ' '.join(mapping.text.strip().split(',')).split()
                if values and values[0].lower() not in ['nm', 'np']:
                    if mapping.name == 'wn':
                        lemma = mapping.attrs.get('lemma', '')
                        version = mapping.attrs.get('version', '')
                        mappings['wn'].append({'lemma': lemma, 'version': version, 'values': values})
                    else:
                        mappings[mapping.name].append(values)

                    print('\t' + mapping.name + str(values))

                    #print(self.fname + str([lemma, values, version]))


        return mappings

if __name__ == '__main__':
    grouping = Groupings('corpora/ontonotes/sense-inventories/')