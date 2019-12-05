# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:51:21 2019

@author: Mijael
"""
import bs4
import re
import json
import os
from itertools import chain
from collections import Counter
from vnclass_args import vnclass_dict

role_mapping = {'cause': 'causer',
                'patient_i': 'patient',
                'patient_j': 'co_patient',
                'agent_i': 'agent',
                'agent_j': 'co_agent',
                'topic_i': 'topic',
                'topic_j': 'co_topic',
                'theme_i': 'theme',
                'theme_j': 'co_theme',
                'location_i': 'location',
                'location_j': 'co_location',
                'source_i': 'source',
                'source_j': 'co_source',
                'recipient_i': 'recipient',
                'recipient_j': 'co_recipient',
                'goal_i': 'goal',
                'goal_j': 'co_goal',
                'v_sound': 'sound',
                'v_instrument': 'instrument',
                'v_direction': 'direction',
                'v_final_state': 'final_state',
                'v_position': 'position',
                'v_material': 'material',
                'v_theme': 'theme',
                'v_manner': 'manner',
                'v_configuration': 'configuration',
                'v_state': 'state',
                'v_result': 'result',
                'v_orientation': 'orientation',
                'v_form': 'form'}

punctuations = "[]{};:\\\,<>./?@#$%^&*~"

def norm_role(role):
    if role:
        if isinstance(role, dict):
            role = {key.lower(): norm_role(them) for key, them in role.items()}
        elif isinstance(role, list):
            role = [norm_role(them) for them in role]
        else:
            role = role.lstrip().rstrip().replace(' ', '_').replace('-', '_').replace('?', '').lower()
            role = remove_punctuations(role)
            role = role_mapping[role] if role in role_mapping else role
    return role

def norm(text):
    if text:
        if isinstance(text, dict):
            text = {key.lower(): norm(val) for key, val in text.items()}
        elif isinstance(text, list):
            text = [norm(val) for val in text]
        else:
            text = text.lstrip().rstrip().replace(' ', '_').replace('?', '').lower()
            text = remove_punctuations(text)
    return text

def remove_punctuations(text):
    for char in punctuations:
        text = text.replace(char, '')

    return text

def tojson(filename, dict):
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=4)

class VerbInspector(object):
    def __init__(self):
        ...

class VerbNet(object):

    def __init__(self, path=''):
        self.path = path
        self.file_names = [f for f in os.listdir(self.path) if f.endswith(".xml")]
        self.soup_files = self.parse()
        self.verb_classes = self.get_verb_classes()
        self.verbs = self.get_verbs()

    def parse(self):
        files = []
        for fname in self.file_names:
            files.append(bs4.BeautifulSoup(open(self.path+fname), "lxml-xml"))
        
        return files
    
    def get_verb_classes(self, class_ids=[]):
        verb_classes = getattr(self, 'verb_classes', {})
        if not verb_classes:
            # Extract every VNCLASS and VNSUBCLASS into a VerbClass object
            for soup in self.soup_files:
                verb_classes[soup.VNCLASS['ID']] = VerbClass(soup.VNCLASS)
                for vnsubclass in soup.find_all('VNSUBCLASS'):
                    verb_classes[vnsubclass['ID']] = VerbClass(vnsubclass)

        if class_ids:
            verb_classes = {class_id: verb_classes[class_id] for class_id in class_ids}

        return verb_classes

    def get_verbs(self):
        verbs = getattr(self, 'verbs', [])
        if not verbs:
            for vclass in self.verb_classes:
                for member in vclass.members:
                    for verb in verbs:
                        if verb.lemma == verb.name:
                        else:



class VerbClass(object):

    def __init__(self, soup=None, json_dict={}):
        self.soup = soup
        self.id = soup['ID']
        self.frames = self.get_frames()
        self.themroles = self.get_themroles()
        self.json_dict = json_dict
        self.class_preds = self.get_class_preds()
        self.class_args = self.get_class_args()
        self.clean_args = self.load_args() if json_dict else self.class_args
        self.clean_preds = self.load_preds() if json_dict else self.class_preds
        self.members = self.get_members()
        #print(self.id)
        #print(self.members)
        #print("'" + self.id + "':" + ''.join([' ' for i in range(len("'" + self.id + "':"),40)]) + str(self.class_args) + ",")

    def get_themroles(self):
        themroles = getattr(self, 'themroles', [])
        if not themroles:
            for themrole in self.soup.THEMROLES.find_all('THEMROLE'):
                role = norm_role(themrole.attrs)
                selrestrs = themrole.find_all('SELRESTRS')

                selrestrs_dict = selrestrs.attrs if hasattr(selrestrs, 'attrs') else {}
                selrestrs_dict['selrestrs'] = []
                for selrestr in themrole.find_all('SELRESTR'):
                    selrestrs_dict['selrestrs'].append(norm(selrestr.attrs))

                themroles.append({'type': role['type'], 'selrestrs': selrestrs_dict})

        return themroles

    def get_frames(self):
        frames = getattr(self, 'frames', [])
        if not frames:
            for frame in self.soup.FRAMES.find_all('FRAME'):
                frames.append(VerbFrame(self.id, frame))

        return frames

    def get_members(self):
        members = getattr(self, 'members', [])
        if not members:
            for member in self.soup.MEMBERS.find_all('MEMBER'):
                members.append(member.attrs)
        return members

    def get_class_args(self):
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

    def get_class_preds(self):
        preds = []
        for frame in self.frames:
            for pred in frame.preds:
                if not any([str(pred) == str(pr) for pr in preds]):
                    preds.append(pred)
        return preds

    def load_args(self):
        # TODO: Load args from JSON
        ...

    def load_args(self):
        # TODO: Load preds from JSON
        ...

class VerbFrame(object):
    def __init__(self, class_id, soup):
        self.class_id = class_id
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
                stx_dict = norm_role(stx.attrs)
                stx_dict['tag'] = stx.name
                stx_dict['synrestrs'] = []
                stx_dict['selrestrs'] = []

                for synrestr in stx.find_all('SYNRESTR'):
                    stx_dict['synrestrs'].append(norm(synrestr.attrs))

                for selrestr in stx.find_all('SELRESTR'):
                    stx_dict['selrestrs'].append(norm(selrestr.attrs))

                syntax.append(stx_dict)

        return syntax

    def get_syntax_args(self):
        syntax_args = getattr(self, 'syntax_args', [])
        if not syntax_args:
            for stx in self.syntax:
                if stx['tag'] == 'NP':
                    syntax_args.append(stx['value'])

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
                bool = '' if 'bool' not in pred.attrs else pred.attrs['bool']
                name = pred.attrs['value']
                preds.append(VerbPredicate(bool, name, pred))

        return preds

class VerbPredicate(object):
    def __init__(self, bool, name, soup):
        self.soup = soup
        self.bool = bool
        self.name = name
        self.args = self.get_args()

    def get_args(self):
        args = getattr(self, 'args', [])
        if not args:
            for arg in self.soup.ARGS.find_all('ARG'):
                # ** There is one case in admire-31.2.xml that a value appears as 'Stimulus, Attribute'
                # in the predicate. I do not know if they will remove this in the future. The next
                # piece of code is to be able to generalize to those kind of cases
                for role in arg.attrs['value'].split(','):
                    args.append({'type': norm(arg.attrs['type']), 'value': norm_role(role)})

        return args

    def get_role_args(self):
        role_args = []
        for arg in self.args:
            if arg['type'] != 'event' and arg['type'] != 'constant':
                role_args.append(arg['value'])
        return role_args

    def __str__(self):
        str = self.bool + self.name + '(' + ','.join([arg['value'] for arg in self.args]) + ')'
        return str

class VerbSense(object):
    def __init__(self, id):
        self.id = id

class Verb(object):
    def __init__(self, lemma):
        self.lemma = lemma
        self.senses = []
        ...
        
    def add_verb_sense(self, class_id, groupings=[], fnframes=[], wn=[]):
        ...
    def __str__(self):
        return self.lemma
        
if __name__ == '__main__':
    vn = VerbNet('../corpora/verbnet/')
    verbs = vn.get_verbs()