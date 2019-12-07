import bs4
import re
import json
import os
from pathlib import Path

# Transform every verbnet themrole into a simpler themrole name
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
                # verbspecific predspecific
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

# Remove this punctuations marks
punctuations = "[]{};:\\\,<>./?@#$%^&*~"


def remove_punctuations(text):
    for char in punctuations:
        text = text.replace(char, '')

    return text


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


def tojson(filename, dict):
    with open(filename, 'w') as outfile:
        json.dump(dict, outfile, indent=4)


def parse_xmls(path, markup='lxml'):
    file_names = [f for f in os.listdir(path) if f.endswith(".xml")]
    files_soup = {}
    for fname in file_names:
        files_soup[fname] = bs4.BeautifulSoup(open(path / fname), markup)

    return files_soup
