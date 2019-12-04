# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:45:02 2019

@author: Mijael
"""

import nltk
import re
import spacy
import json
import xml.etree.ElementTree as ET
from collections import defaultdict
from allennlp.predictors.predictor import Predictor
from spacy.matcher import Matcher
from nltk.chunk import RegexpParser
from difflib import SequenceMatcher
from nltk.corpus import treebank
from nltk.corpus import propbank as pb
import xmltodict

# Load verbnet3.3
verbnet3 = nltk.corpus.util.LazyCorpusLoader(
    'verbnet3.3', nltk.corpus.reader.verbnet.VerbnetCorpusReader,
    r'(?!\.).*\.xml')

# Load propbank (latest version)
propbank = nltk.corpus.util.LazyCorpusLoader(
    'propbank2.0',
    nltk.corpus.reader.propbank.PropbankCorpusReader,
    'prop.txt',
    'frames/.*\.xml',
    'verbs.txt',
    lambda filename: re.sub(r'^wsj/\d\d/', '', filename),
    treebank,
)  

# Additional thematic roles - mappings
additional_themrole_mapping = {'cause': 'causer',
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
                               'goal_j': 'co_goal'}

verbspecific = {'v_instrument': 'instrument',
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
                'v_form': 'form',
                'v_sound': 'sound'
}
# These are punctuations marks that attributes in propbank and verbnet shouldn't have
punctuations = "[]{};:\\\,<>./?@#$%^&*~"

def norm_value(value):
    if isinstance(value,dict):
        value = {key.lower(): norm_value(val) for key,val in value.items()}
    elif isinstance(value, list):
        value = [norm_value(val) for val in value]
    else:
        if value:
            value = value.lstrip().rstrip()
            value = value.replace(' ', '_').replace('?', '').lower()
            value = remove_punctuations(value)
            
    return value

def norm_themrole(themrole):
    """ """
    if isinstance(themrole,dict):
        themrole = {key.lower(): norm_themrole(them) for key,them in themrole.items()}
    elif isinstance(themrole, list):
        themrole = [norm_themrole(them) for them in themrole]
    else:
        if themrole:
            themrole = themrole.lstrip().rstrip()
            themrole = themrole.replace(' ', '_').replace('-', '_').replace('?', '').lower()
            themrole = remove_punctuations(themrole)
            if themrole in additional_themrole_mapping:
                themrole = additional_themrole_mapping[themrole]
                
            if themrole in verbspecific:
                themrole = verbspecific[themrole]
            
    return themrole

def remove_punctuations(text):
    for char in punctuations:
        text=text.replace(char,'')
        
    return text


# Verbnet to dictionary
# It might be still incomplete
verb_class = dict()
for class_id in verbnet3.classids():
    vnclass = verbnet3.vnclass(class_id)
    #print(json.dumps(xmltodict.parse(ET.tostring(vnclass, encoding='utf8', method='xml'))))
    verb_class[class_id] = dict()
    
    verb_class[class_id]['members'] = list()
    for el in vnclass.findall('MEMBERS/MEMBER'):
        #(el.attrib)
        verb_class[class_id]['members'].append(el.attrib)
    
    verb_class[class_id]['themroles'] = list()
    for el in vnclass.findall('THEMROLES/THEMROLE'):
         themrole = norm_themrole(el.attrib)
         themrole['selrestrs'] = list()
         #themrole['synrestrs'] = list()
         for sel in el.findall('SELRESTRS/SELRESTR'):
             themrole['selrestrs'].append(norm_value(sel.attrib))
             
         #for syn in el.findall('SYNRESTRS/SYNRESTR'):
            # themrole['synrestrs'].append(norm_value(syn.attrib))
         verb_class[class_id]['themroles'].append(themrole)
         
    verb_class[class_id]['frames'] = list()
    for el in vnclass.findall('FRAMES/FRAME'):
         frame = dict()
         
         frame['description'] = el.findall('DESCRIPTION')[0].attrib
         frame['examples'] = list()
         for ie in el.findall('EXAMPLES/EXAMPLE'):
             frame['examples'].append(ie.text)
        
         frame['syntax'] = list()
         for stx in el.find('SYNTAX'):
             dict_syntax = norm_value(stx.attrib)
             dict_syntax['tag'] = norm_value(stx.tag)
             dict_syntax['synrestrs'] = list()
             dict_syntax['selrestrs'] = list()
             
             for sel in stx.findall('SELRESTRS/SELRESTR'):
                 dict_syntax['selrestrs'].append(norm_value(sel.attrib))
                 
             for syn in stx.findall('SYNRESTRS/SYNRESTR'):
                 dict_syntax['synrestrs'].append(norm_value(syn.attrib))
            
                 
             frame['syntax'].append(dict_syntax)
             
         frame['predicates'] = list()    
         for pred in el.findall('SEMANTICS/PRED'):
             dict_predicates = norm_value(pred.attrib)
             dict_predicates['args'] = list()
             for arg in pred.findall('ARGS/ARG'):
                 dict_predicates['args'].append(norm_themrole(arg.attrib))
                 
             frame['predicates'].append(dict_predicates)
                 
         verb_class[class_id]['frames'].append(frame)

# Propbank to Dictionary
# It might be still incomplete

verb_pb = dict()
for role in propbank.rolesets():
    id_ = role.attrib['id']
    verb_pb[id_] = role.attrib
    verb_pb[id_]['aliases'] = list()
    for alias in role.findall('aliases/alias'):
        al = alias.attrib
        al['propbank'] = alias.text
        verb_pb[id_]['aliases'].append(al)
    
    verb_pb[id_]['notes'] = list()
    for note in role.findall('note'):
        verb_pb[id_]['notes'].append(note.text)
    
    verb_pb[role.attrib['id']]['roles'] = list()
    for roles in role.findall('roles/role'):
        role_dict = roles.attrib
        role_dict['vnroles'] = list()
        for vnrole in roles.findall('vnrole'):
            role_dict['vnroles'].append(vnrole.attrib)
            
        verb_pb[id_]['roles'].append(role_dict)
    
    verb_pb[role.attrib['id']]['examples'] = list()
    for exa in role.findall('example'):
        dict_example = exa.attrib
        dict_example['args'] = list()
        for ex in exa:
            if ex.tag == 'inflection':
                dict_example['inflection'] = ex.attrib
            elif ex.tag == 'text':
                dict_example['text'] = ex.text
            else:
                dict_arg = ex.attrib
                dict_arg['tag'] = ex.tag
                dict_arg['text'] = ex.text  
                dict_example['args'].append(dict_arg)
                
        verb_pb[role.attrib['id']]['examples'].append(dict_example)
    
# Store json file
with open('verbnet33.json', 'w') as outfile:
    json.dump(verb_class, outfile, indent=4)
    
with open('propbank.json', 'w') as outfile:
    json.dump(verb_pb, outfile, indent=4)
    