import bs4
import re
import json
import os
import sys
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

pb_argm = {'com': 'Comitative',
           'loc': 'Locative',
           'dir': 'Directional',
           'dsp': 'Direct Speech',
           'gol': 'Goal',
           'mnr': 'Manner',
           'ext': 'Extent',
           'rec': 'Reciprocal',
           'pnc': 'Purpose Not Cause',
           'prd': 'Secondary Predication',
           'prp': 'Purpose',
           'prr': 'Predicating Relation',
           'ppt': 'Proto Patient',
           'pag': 'Proto Agent',
           'cau': 'Cause',
           'dis': 'Discourse',
           'vsp': 'Verb Specific',
           'adv': 'Adverbial',
           'adj': 'Adjectival',
           'mod': 'Modal',
           'neg': 'Negation',
           'dsp': 'Direct Speech',
           'slc': 'Relative Clause',
           'lvb': 'Light Verb',
           'tmp': 'Temporal'}

pbvn_themrole_mappings = {'pag': ['agent', 'causer', 'pivot', 'stimulus'],
                          'mnr': ['asset', 'instrument', 'manner'],
                          'prd': ['attribute', 'predicate', 'product'],
                          'gol': ['beneficiary', 'goal', 'destination', 'direction', 'goal', 'recipient', 'trajectory'],
                          'com': ['co_agent', 'beneficiary'],
                          'ppt': ['co_theme', 'patient', 'theme', 'experiencer', 'reflexive', 'topic'],
                          'dir': ['destination', 'direction', 'initial_location', 'source', 'trajectory'],
                          'tmp': ['duration', 'time', 'final_time'],
                          'ext': ['extent'],
                          'loc': ['initial_location', 'location'],
                          'dis': ['agent']}

# Possible fillers for thematic roles
starting_point = ['source', 'initial_state', 'initial_location']
ending_point = ['goal', 'result', 'product', 'destination', 'final_time',
                'recipient', 'trajectory', 'v_final_state']

# The frame possibly needs an agent
agentive = ['agent', 'causer']

# When using this preposition is a prep_type
prep_type = ['about', 'above', 'after', 'against', 'among', 'as', 'at', 'back', 'beside',
             'before', 'below', 'between', 'by', 'concerning', 'for', 'from', 'if', 'in',
             'in between', 'into', 'like', 'of', 'off', 'on', 'onto', 'out', 'out of',
             'over', 'regarding', 'respecting', 'though', 'through', 'to', 'towards',
             'under', 'until', 'upon', 'with']

# Possible location thematic role when using these prepositions
preps_location = ['about', 'above', 'against', 'along', 'amid', 'among', 'amongst', 'around',
                  'astride', 'at', 'athwart', 'back', 'before', 'behind', 'below', 'beneath',
                  'beside', 'between', 'beyond', 'by', 'from', 'in', 'in between', 'in front of',
                  'inside', 'into', 'near', 'next to', 'off', 'on', 'onto', 'opposite', 'out of',
                  'outside', 'over', 'round', 'through', 'throughout', 'to', 'towards', 'under',
                  'underneath', 'upon', 'within']

# Possible trajectory thematic role when using these prepositions
preps_trajectory = ['above', 'across', 'along', 'around', 'back', 'below', 'beside', 'between',
                    'down', 'in between', 'over', 'past', 'round', 'through', 'towards', 'under',
                    'up']

# Possible source thematic role when using these prepositions
preps_source = ['from', 'off', 'off of', 'out', 'out of']

# Possible desination thematic role when using these preopsitions
preps_destination = ['at', 'for', 'into', 'on', 'onto', 'to', 'towards']

# It is simply 'to' when using this prepositions.
to = ['into', 'to', 'onto']

# Possible clause phrase
clauses_dep = ['advcl', 'acl', 'csubj', 'ccomp', 'xcomp']

# All the possible thematic roles and preposition type from the list of prepositions
maybe_themroles = ['location', 'trajectory', 'source', 'destination', 'to']

# It is not a location for this two propbank argument types
not_location = ['PRP', 'MNR']

# Correcting errors in datasets
class_name_typos = {'judgement': 'judgment',
                    'occurrence': 'occur',
                    'crave': 'carve',
                    'spacial_configuration': 'spatial_configuration',
                    'clasify': 'classify',
                    'contguous_location': 'contiguous_location',
                    'modes_of_being_with_mothion': 'modes_of_being_with_motion',
                    'noverbal_expression': 'nonverbal_expression',
                    'skid': 'run',
                    'temporal_configuration': 'occur',
                    'approve': 'accept',
                    'sastify': 'satisfy'}

class_name = {'settle-89': ['harmonize-22.6', 'acquiesce-95.1-1', 'hire-13.5.3'],
              'force-59': ['urge-58.1-1-1', 'compel-59.1', 'stimulate-59.4', 'trick-59.2', 'urge-58.1-1'],
              'force-59.1': ['compel-59.1'],
              'force-59-1': ['compel-59.1', 'trick-59.2']}

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
    if filename:
        with open(filename, 'w') as outfile:
            json.dump(dict, outfile, indent=3)


def fromjson(filename):
    if filename:
        try:
            with open(filename) as json_file:
                data = json.load(json_file)

            return data
        except FileNotFoundError:
            return {}

    return {}


def flatten(data):
    newlist = []
    if isinstance(data, list):
        for dt in data:
            newlist = newlist + flatten(dt)
    else:
        return [data]
    return newlist


def parse_xmls(path, markup='lxml'):
    file_names = [f for f in os.listdir(path) if f.endswith(".xml")]
    files_soup = {}
    for fname in file_names:
        files_soup[fname] = bs4.BeautifulSoup(open(path / fname), markup)

    return files_soup


def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)


def deep_update(x, y):
    for key in y.keys():
        if key not in x:
            x.update({key: y[key]})
        elif x[key] != y[key]:
            if isinstance(x[key], dict):
                x.update({key: deep_update(x[key], y[key])})
            else:
                x.update({key: list(set(x[key] + y[key]))})
    return x


def vnpb_mappings_check_vn(mappings, vn):
    for lemma in mappings:
        for mapping in lemma['mappings']:
            for map in mapping['mappings']:
                clss = vn.get_class(map['vncls'])
                if not clss:
                    print(f' {lemma["lemma"]} Not found {map["vncls"]}')


def get_classes_from_vnpb_mappings(mappings, lemma, roleset):
    vncls = []
    for mps in mappings:
        if mps['lemma'] == lemma:
            for mapping in mps['mappings']:
                if mapping['id'] == roleset:
                    for map in mapping['mappings']:
                        vncls.append(map['vncls'])
                    break
    return vncls


def replace_missing_classes_in_propbank(vnpb, vn, pb):
    vnclasses = list(vn.classes.keys())
    for predicate in pb.predicates.values():
        for roleset in predicate.get_rolesets():
            classes = roleset.get_classes()
            for cls in classes:
                res = ''
                for vncls in vnclasses:
                    tupl = re.match(r'(\w+)-(.*)', vncls)
                    if tupl[2] == cls:
                        res = cls

                if not res:
                    vnpb_classes = get_classes_from_vnpb_mappings(vnpb, predicate.lemma, roleset.id)
                    print(f'{predicate.lemma} {roleset.id} Not found {cls}, but found {str(vnpb_classes)}')
                    sys.stdout.write('Select:')
                    choice = input().lower()
                    if choice:
                        pb.replace(f'vncls="{cls}"', f'vncls="{choice}"', predicate.lemma)


def replace_missing_classes_in_grouping(vn, gr, class_id, lemma, sense):
    classes = list(vn.get_classes(lemma).keys())
    print(sense + ' ' + lemma + ' Not found: ' + class_id)
    print(classes)
    tupl = re.match(r'(\w+)-(.*)', class_id)
    if tupl:
        cls, id = (tupl[1], tupl[2])
        id_ = re.sub(r'-\d', '', id)
        res = ''
        print(cls + ' ' + id)
        if class_id in class_name:
            for cls_id in class_name[class_id]:
                if cls_id in classes:
                    res = cls_id
                    print(f'{class_id} is {res}')
                    break

        if not res:
            for cls_id in classes:
                if cls in class_name_typos:
                    cls = class_name_typos[cls]

                if cls in cls_id:
                    res = cls_id
                    print(f'{class_id} is {res}')
                    break

        if not res:
            if class_id in class_name:
                for cls_id in class_name[class_id]:
                    if cls_id in vn.classes:
                        res = cls_id
                        print(f'{class_id} is {res}')
                        break

        if not res:
            for cls_id in vn.classes:
                if cls in class_name_typos:
                    cls = class_name_typos[cls]

                tupl = re.match(r'(\w+)-(.*)', cls_id)
                if cls == tupl[1]:
                    res = cls_id
                    print(f'{class_id} is {res}')
                    break

        if not res:
            for cls_id in classes:
                if id in cls_id or id_ in cls_id:
                    res = cls_id
                    print(f'{class_id} is {res}')
                    break

        if not res:
            for cls_id in vn.classes:
                if '-' + id in cls_id or '-' + id_ in cls_id:
                    res = cls_id
                    print(f'{class_id} is {res}')
                    break

        if not res and len(classes) == 1:
            res = classes[0]
            print(f'{class_id} is {res}')

    if res:
        if query_yes_no('Edit?'):
            gr.replace(class_id, res, lemma)


def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def replace(str_, forstr_, filename):
    with open(filename, "rt") as f:
        newText = f.read().replace(str_, forstr_)

    with open(filename, "w") as f:
        f.write(newText)


def indent(n):
    return ''.join(['\t' for i in range(0, n)])


def write(file, string, mode):
    with open(file, mode) as f:
        f.write(string)

# def pprint(obj, indent=0, end='\n'):
#     indent_in = indent(indent)
#     indent_ = indent(indent + 1)
#     str_ = f''
#     for key, value in obj.__dict__.items():
#         if isinstance(value, str) or isinstance(value, int):
#             str_ += f'{indent_}{key}={value}{end}'
#         elif isinstance(value, list):
#             for el in value:
#                 if not isinstance(el, str) and not isinstance(el, int):
#                     str_ += f'{el.pprint(indent+1, end)}'
#                 else:
#                     str_ +
#         elif isinstance(value, dict):


# def vnpb_mappings_check_pb(mappings, vn):
