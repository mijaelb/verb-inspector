vnclass_preds_dict = {
'absorb-39.8': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'goal'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'accept-77.1': [
                   { 'value': 'approve', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'accompany-51.7': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'ee3'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'acquiesce-95.1': [
                   { 'value': 'yield', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'yield', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'acquiesce-95.1-1': [
                   { 'value': 'yield', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'act-114': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'predicate'}]}
],
'act-114-1': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'predicate'}]}
],
'act-114-1-1': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'predicate'}]}
],
'addict-96': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'desire', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'adjust-26.9': [
                   { 'bool': '!', 'value': 'adjusted', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'adjusted', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'admire-31.2': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus_attribute'}]}
],
'admire-31.2-1': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'admit-64.3': [
                   { 'value': 'admit', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'admit-64.3-1': [
                   { 'value': 'admit', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'adopt-93': [
                   { 'value': 'adopt', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'advise-37.9': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'advise-37.9-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'allow-64.1': [
                   { 'value': 'allow', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'allow-64.1-1': [
                   { 'value': 'allow', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'amalgamate-22.2': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'amalgamate-22.2-1': [
                   { 'bool': '!', 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'amalgamate-22.2-1-1': [
                   { 'bool': '!', 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'amalgamate-22.2-2': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'amalgamate-22.2-2-1': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'amalgamate-22.2-3': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'amalgamate-22.2-3-1': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'amalgamate-22.2-3-1-1': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'amalgamate-22.2-3-2': [
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'amuse-31.1': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'verbspecific', 'value': 'emotion'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'verbspecific', 'value': 'emotion'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'animal_sounds-38': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_sound'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'appeal-31.4': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'appeal-31.4-1': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'appeal-31.4-2': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'appeal-31.4-3': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'appear-48.1.1': [
                   { 'value': 'appear', 'args': [
                                       {'type': 'event', 'value': 'during(e)'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'start(e)'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'end(e)'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'appoint-29.1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'designated', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'assessment-34.1': [
                   { 'value': 'assess', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'assuming_position-50': [
                   { 'bool': '!', 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'body_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'attack-60.1': [
                   { 'value': 'conflict', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'hostile'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '?', 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'attack-60.1-1': [
                   { 'value': 'conflict', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'bool': '?', 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'constant', 'value': 'forceful'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'attend-107.4': [
],
'attend-107.4-1': [
                   { 'value': 'set_member', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'attend-107.4-2': [
                   { 'value': 'set_member', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'avoid-52': [
                   { 'value': 'avoid', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'avoid', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'banish-10.2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'base-97.1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'base', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'battle-36.4': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'conflict', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'bool': '?', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'constant', 'value': 'hostile'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'about', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'about', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'battle-36.4-1': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'conflict', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'bool': '?', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'constant', 'value': 'hostile'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'about', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'become-109.1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'become-109.1-1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'become-109.1-1-1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'beg-58.2': [
                   { 'value': 'urge', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'beg-58.2-1': [
                   { 'value': 'urge', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'beg-58.2-1-1': [
                   { 'value': 'urge', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'begin-55.1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'begin', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'begin-55.1-1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'begin', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'begin-55.1-1-1': [
                   { 'value': 'begin', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'being_dressed-41.3.3': [
                   { 'value': 'wear', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'bend-45.2': [
                   { 'bool': '!', 'value': 'physical_form', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'physical_form', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'physical_form', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'benefit-72.2': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'berry-13.7': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'predspecific', 'value': 'source'},
                                       {'type': 'verbspecific', 'value': 'v_theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'predspecific', 'value': 'source'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'predspecific', 'value': 'source'},
                                       {'type': 'verbspecific', 'value': 'v_theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'predspecific', 'value': 'source'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'bill-54.5': [
                   { 'value': 'financial_relationship', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'birth-28.2': [
                   { 'bool': '!', 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'birth-28.2-1': [
                   { 'bool': '!', 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'body_internal_motion-49.1': [
                   { 'value': 'body_motion', 'args': [
                                       {'type': 'event', 'value': 'ë'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'body_internal_states-40.6': [
                   { 'value': 'body_reflex', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'involuntary', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'body_motion-49.2': [
                   { 'bool': '!', 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'body_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'path'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'body_motion-49.2-1': [
                   { 'bool': '!', 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'body_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'path'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'body_motion-49.2-1-1': [
                   { 'bool': '!', 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'body_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'path'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'braid-41.2.2': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'break-45.1': [
                   { 'bool': '!', 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'bool': '!', 'value': 'physical_form', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'physical_form', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'physical_form', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'break_down-45.8': [
                   { 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'breathe-40.1.2': [
                   { 'value': 'body_process', 'args': [
                                       {'type': 'event', 'value': 'ee1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'event', 'value': 'ee1'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'source'}]},
                   { 'value': 'body_process', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'source'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'ee2'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'breathe-40.1.2-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'source'}]},
                   { 'value': 'body_process', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'source'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'ee2'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'bring-11.3': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'bring-11.3-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'build-26.1': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'made_of', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'themrole', 'value': 'material'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]},
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'cost', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'build-26.1-1': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'made_of', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'themrole', 'value': 'material'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'cost', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'bulge-47.5.3': [
                   { 'value': 'filled_with', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'bully-59.5': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'result'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'constant', 'value': 'hostile'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'bump-18.4': [
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'constant', 'value': 'directedmotion'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'forceful'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'bump-18.4-1': [
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'constant', 'value': 'directedmotion'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'directedmotion'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'forceful'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'forceful'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'butter-9.9': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'calibratable_cos-45.6.1': [
                   { 'value': 'has_val', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'predspecific', 'value': 'initial_state'}]},
                   { 'value': 'change_value', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_direction'},
                                       {'type': 'predspecific', 'value': 'extent'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'has_val', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'predspecific', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_property', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'calibratable_cos-45.6.1-1': [
                   { 'value': 'has_val', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'initial_state'}]},
                   { 'value': 'change_value', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_direction'},
                                       {'type': 'themrole', 'value': 'extent'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'has_val', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_property', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'calve-28.1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'give_birth', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'captain-29.8': [
                   { 'value': 'masquerade', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'role'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'captain-29.8-1': [
                   { 'value': 'masquerade', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'role'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'captain-29.8-1-1': [
                   { 'value': 'masquerade', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'role'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'care-88.1': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'care-88.1-1': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'caring-75.2': [
],
'caring-75.2-1': [
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'caring-75.2-1-1': [
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'caring-75.2-2': [
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'carry-11.4': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]}
],
'carry-11.4-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]}
],
'carry-11.4-1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]}
],
'carve-21.2': [
],
'carve-21.2-1': [
                   { 'bool': '!', 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'bool': '!', 'value': 'physical_form', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_form'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'physical_form', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_form'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'physical_form', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_form'}]}
],
'carve-21.2-2': [
                   { 'bool': '!', 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'movement'}]},
                   { 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'carve-21.2-3': [
                   { 'bool': '!', 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_instrument'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'verbspecific', 'value': 'v_instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'caused_calibratable_cos-45.6.2': [
                   { 'value': 'has_val', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'initial_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'change_value', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_direction'},
                                       {'type': 'themrole', 'value': 'extent'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'has_val', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'meets', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_property', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'caused_calibratable_cos-45.6.2-1': [
                   { 'value': 'has_val', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'initial_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'change_value', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_direction'},
                                       {'type': 'themrole', 'value': 'extent'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'has_val', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'meets', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_property', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'change_value', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_direction'},
                                       {'type': 'themrole', 'value': 'extent'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'has_val', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'change_bodily_state-40.8.4': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'predspecific', 'value': 'v_final_state'}]},
                   { 'value': 'body_reflex', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'involuntary', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'predspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'characterize-29.2': [
                   { 'value': 'characterize', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'characterize-29.2-1': [
                   { 'value': 'describe', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'characterize-29.2-1-1': [
                   { 'value': 'describe', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'characterize-29.2-1-2': [
                   { 'value': 'describe', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'chase-51.6': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'destination'}]}
],
'cheat-10.6.1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'cheat-10.6.1-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'cheat-10.6.1-1-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'chew-39.2': [    { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'chew-39.2-1': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'chew-39.2-2': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'chit_chat-37.6': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'co_topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'co_topic'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'repeated_sequence', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e4'}]}
],
'chit_chat-37.6-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'co_topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'co_topic'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'repeated_sequence', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e4'}]}
],
'classify-29.10': [
                   { 'value': 'group', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'clear-10.3': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'clear-10.3-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'cling-22.5': [
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'cognize-85': [
                   { 'value': 'understand', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'coil-9.6': [
                   { 'bool': '!', 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'value': 'elliptical_motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'axis'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'destination'},
                                       {'type': 'themrole', 'value': 'axis'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'destination'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'value': 'elliptical_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'axis'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'destination'}]}
],
'coil-9.6-1': [
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'adv', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'verbspecific', 'value': 'prop'}]},
                   { 'value': 'has_property', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'prop'}]}
],
'coloring-24': [
                   { 'bool': '!', 'value': 'covered', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_material'}]},
                   { 'value': 'apply_material', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_material'}]},
                   { 'value': 'covered', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_material'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'compel-59.1': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'predicate'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'complain-37.8': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'complete-55.2': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'end', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'complete-55.2-1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'end', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'comprehend-87.2': [
                   { 'value': 'understand', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'has_property', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'comprehend-87.2-1': [
                   { 'value': 'understand', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'comprehend-87.2-1-1': [
                   { 'value': 'understand', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'comprehend-87.2-1-1-1': [
                   { 'value': 'understand', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'comprise-107.2': [
],
'comprise-107.2-1': [
                   { 'value': 'has_set_member', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'comprise-107.2-2': [
                   { 'value': 'has_set_member', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'concealment-16': [
                   { 'value': 'visible', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'visible', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'concealment-16-1': [
                   { 'value': 'visible', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'bool': '!', 'value': 'visible', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'bool': '!', 'value': 'visible', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'conduct-111.1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'occur', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'confess-37.10': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'confine-92': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'bool': '!', 'value': 'confined', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'confined', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'confine-92-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'bool': '!', 'value': 'confined', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'confined', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'confront-98': [
                   { 'value': 'confront', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'instrument'}]}
],
'conjecture-29.5': [
                   { 'value': 'believe', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'predicate'}]}
],
'conjecture-29.5-1': [
                   { 'value': 'believe', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'predicate'}]}
],
'conjecture-29.5-2': [
                   { 'value': 'believe', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'predicate'}]}
],
'consider-29.9': [
                   { 'value': 'consider', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'consider-29.9-1': [
                   { 'value': 'characterize', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'consider', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'consider-29.9-1-1': [
                   { 'value': 'characterize', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'consider', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'consider-29.9-1-1-1': [
                   { 'value': 'consider', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'characterize', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'consider-29.9-2': [
                   { 'value': 'characterize', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'consider', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'conspire-71': [
                   { 'value': 'conspire', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'conspire', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'consume-66': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'spend', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'consume-66-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'spend', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'contain-15.4': [
                   { 'value': 'contain', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'contiguous_location-47.8': [
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'contiguous_location-47.8-1': [
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'contiguous_location-47.8-2': [
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'continue-55.3': [
                   { 'value': 'continue', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'event', 'value': 'e'}]},
                   { 'value': 'time', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'final_time'}]}
],
'contribute-13.2': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'contribute-13.2-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'contribute-13.2-1-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'contribute-13.2-2': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'contribute-13.2-2-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'convert-26.6.2': [
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'initial_state'}]},
                   { 'value': 'convert', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'opposition', 'args': [
                                       {'type': 'themrole', 'value': 'initial_state'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'convert-26.6.2-1': [
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'initial_state'}]},
                   { 'value': 'convert', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'opposition', 'args': [
                                       {'type': 'themrole', 'value': 'initial_state'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'convert-26.6.2-1-1': [
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'initial_state'}]},
                   { 'value': 'convert', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'opposition', 'args': [
                                       {'type': 'themrole', 'value': 'initial_state'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'convert', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e4'}]}
],
'cooking-45.3': [
                   { 'bool': '!', 'value': 'cooked', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'apply_heat', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'cooked', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'cooperate-73.1': [ 
                    { 'value': 'cooperate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'cooperate-73.1-1': [
                   { 'value': 'cooperate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'cooperate-73.1-2': [
                   { 'value': 'cooperate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'cooperate-73.1-3': [
                   { 'value': 'cooperate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'cope-83': [
                   { 'value': 'cope', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'cope-83-1': [
                   { 'value': 'cope', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'cope-83-1-1': [
                   { 'value': 'cope', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'correlate-86.1': [
                   { 'value': 'correlated', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'bool': '!', 'value': 'correlated', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'correlated', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'correspond-36.1.1': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'about', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'correspond-36.1.1-1': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'about', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'correspond-36.1.1-1-1': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'about', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'cost-54.2': [
                   { 'value': 'value', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'value'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'crane-40.3.2': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'bool': '!', 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'bool': '!', 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'body_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'create-26.4': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]},
                   { 'value': 'property', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'result'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'create-26.4-1': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'create-26.4-1-1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'curtsey-40.3.3': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'bool': '!', 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'bool': '!', 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'predspecific', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'body_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'predspecific', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'cut-21.1': [
                   { 'bool': '!', 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'movement'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'movement'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'cut-21.1-1': [
                   { 'bool': '!', 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'},
                                       {'type': 'verbspecific', 'value': 'movement'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'causer'}]},
                   { 'value': 'experience', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'degradation_material_integrity', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'debone-10.8': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'declare-29.4': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'declare-29.4-1': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'declare-29.4-1-1': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'declare-29.4-1-1-1': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'declare-29.4-1-1-2': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'declare-29.4-1-1-3': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'declare-29.4-2': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'dedicate-79': [
                   { 'value': 'dedicate', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'deduce-97.2': [
                   { 'value': 'conclude', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'defend-72.3': [
                   { 'value': 'defend', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'beneficiary'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'deprive-10.6.2': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'destroy-44': [
                   { 'bool': '!', 'value': 'destroyed', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'destroyed', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]}
],
'devour-39.4': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'die-42.4': [
                   { 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'bool': '!', 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'die-42.4-1': [
                   { 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'bool': '!', 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'differ-23.4': [
                   { 'value': 'different', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'dine-39.5': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'disappearance-48.2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'disappear', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]}
],
'disappearance-48.2-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'disappear', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]}
],
'disassemble-23.3': [
                   { 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'bool': '!', 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'discover-84': [
                   { 'value': 'discover', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'discover-84-1': [
                   { 'value': 'discover', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'discover-84-1-1': [
                   { 'value': 'discover', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'disfunction-105.2.2': [
                   { 'value': 'function', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'function', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'distinguish-23.5': [
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'different', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'distinguish-23.5-1': [
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'different', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'dress-41.1.1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'dressing_well-41.3.2': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'drive-11.5': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]}
],
'drive-11.5-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]}
],
'dub-29.3.2': [
                   { 'bool': '!', 'value': 'designated', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'designated', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'earn-54.6': [
                   { 'value': 'earn', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'eat-39.1': [
],
'eat-39.1-1': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'eat-39.1-2': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'eat-39.1-3': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'empathize-88.2': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'employment-95.3': [
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'beneficiary'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]},
                   { 'value': 'work', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'encounter-30.5': [
                   { 'value': 'perceive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'enforce-63': [
                   { 'value': 'enforce', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'engender-27.1': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'precondition'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'engender-27.1-1': [
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'precondition'}]},
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'predicate'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'ensure-99': [
                   { 'value': 'ensure', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'precondition'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'entity_specific_cos-45.5': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]}
],
'entity_specific_modes_being-47.2': [
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'equip-13.4.2': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'equip-13.4.2-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'equip-13.4.2-1-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'escape-51.1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'escape-51.1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'escape-51.1-1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'escape-51.1-1-2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'escape-51.1-1-3': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'establish-55.5': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'establish-55.5-1': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'estimate-34.2': [
                   { 'value': 'assess', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'value'}]}
],
'estimate-34.2-1': [
                   { 'value': 'assess', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'value'}]}
],
'exceed-90': [
                   { 'value': 'exceed', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'exchange-13.6.1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e5'}]}
],
'exclude-107.3': [
                   { 'bool': '!', 'value': 'involve', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'exclude-107.3-1': [
                   { 'bool': '!', 'value': 'involve', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'exhale-40.1.3': [
],
'exhale-40.1.3-1': [
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'body_process', 'args': [
                                       {'type': 'event', 'value': 'ee1'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'exhale-40.1.3-2': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'ee1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'body_process', 'args': [
                                       {'type': 'event', 'value': 'ee1'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'exist-47.1': [
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'exist-47.1-1': [
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'circumstance'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'circumstance'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'manner'}]}
],
'feeding-39.7': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'ferret-35.6': [
                   { 'value': 'search', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'fill-9.8': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'fill-9.8-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'fire-10.10': [
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'bool': '!', 'value': 'authority_relationship', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'fit-54.3': [
                   { 'value': 'capacity', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'value'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'capacity', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'value'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'themrole', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'flinch-40.5': [
                   { 'bool': '!', 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'predspecific', 'value': 'position'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'involuntary', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'body_reflex', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'predspecific', 'value': 'position'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'floss-41.2.1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]}
],
'focus-87.1': [
                   { 'value': 'think', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'focus-87.1-1': [
                   { 'value': 'think', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'forbid-64.4': [
                   { 'bool': '!', 'value': 'allow', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'forbid-64.4-1': [
                   { 'bool': '!', 'value': 'allow', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'free-10.6.3': [
                   { 'bool': '!', 'value': 'free', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'free', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'free-10.6.3-1': [
                   { 'bool': '!', 'value': 'free', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'free', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'free-10.6.3-1-1': [
                   { 'bool': '!', 'value': 'free', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'free', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'fulfilling-13.4.1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'fulfilling-13.4.1-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'fulfilling-13.4.1-2': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'function-105.2.1': [
                   { 'value': 'function', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'function-105.2.1-1': [
                   { 'value': 'function', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_property', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'predicate'}]}
],
'funnel-9.3': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'funnel-9.3-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'funnel-9.3-1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'future_having-13.3': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'goal'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'goal'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'irrealis', 'args': [
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'irrealis', 'args': [
                                       {'type': 'event', 'value': 'e3'}]}
],
'get-13.5.1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e5'}]},
                   { 'value': 'cost', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'get-13.5.1-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'cost', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'give-13.1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'give-13.1-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'asset'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e5'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'cost', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'gobble-39.3': [
                    { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
                    
],
'gobble-39.3-1': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'gobble-39.3-2': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'gorge-39.6': [
                   { 'value': 'take_in', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'groom-41.1.2': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'predspecific', 'value': 'v_final_state'}]},
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'predspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'grow-26.2.1': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'develop', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'becomes', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'develop', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'becomes', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'harmonize-22.6': [
                   { 'value': 'harmonize', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'help-72.1': [ { 'value': 'help', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'beneficiary'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'help-72.1-1': [
                   { 'value': 'help', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'beneficiary'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'help-72.1-1-1': [
                   { 'value': 'help', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'beneficiary'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'help-72.1-2': [
                   { 'value': 'help', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'beneficiary'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'herd-47.5.2': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'hiccup-40.1.1': [
                   { 'value': 'body_process', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'involuntary', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'hire-13.5.3': [
                   { 'bool': '!', 'value': 'authority_relationship', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'predspecific', 'value': 'goal'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'predspecific', 'value': 'goal'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'hit-18.1': [
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'constant', 'value': 'directedmotion'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'constant', 'value': 'forceful'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'constant', 'value': 'directedmotion'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'constant', 'value': 'forceful'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'constant', 'value': 'directedmotion'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'constant', 'value': 'directedmotion'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'constant', 'value': 'forceful'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'constant', 'value': 'forceful'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e4'}]}
],
'hit-18.1-1': [
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'constant', 'value': 'directedmotion'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'constant', 'value': 'directedmotion'}]}
],
'hold-15.1': [
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'continue', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'hunt-35.1': [
                   { 'value': 'search', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'hurt-40.8.3': [
],
'hurt-40.8.3-1': [
                   { 'bool': '!', 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'body_sensation', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'experiencer'}]}
],
'hurt-40.8.3-1-1': [
                   { 'bool': '!', 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'body_sensation', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'experiencer'}]}
],
'hurt-40.8.3-2': [
                   { 'bool': '!', 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'body_sensation', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'predspecific', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'illustrate-25.3': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'create_image', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'image_impression-25.1': [
                   { 'bool': '!', 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'create_image', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'indicate-78': [
                   { 'value': 'indicate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'indicate-78-1': [
                   { 'value': 'indicate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'perceive', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'indicate-78-1-1': [
                   { 'value': 'indicate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'initiate_communication-37.4.2': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'predspecific', 'value': 'topic'}]}
],
'initiate_communication-37.4.2-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'predspecific', 'value': 'topic'}]}
],
'inquire-37.1.2': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'bool': '!', 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'instr_communication-37.4.1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'intend-61.2': [
                   { 'value': 'intend', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'characterize', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'intend-61.2-1': [
                   { 'value': 'intend', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'intend-61.2-1-1': [
                   { 'value': 'intend', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'interact-36.6': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]}
],
'interrogate-37.1.3': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'bool': '!', 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'property', 'args': [
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'invest-13.5.4': [
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'financial_interest_in', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'invest-13.5.4-1': [
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'financial_interest_in', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'investigate-35.4': [
                   { 'value': 'search', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'involve-107.1': [
                   { 'value': 'involve', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'judgment-33.1': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'judgment-33.1-1': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'judgment-33.1-1-1': [
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'keep-15.2': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'knead-26.5': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'made_of', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'themrole', 'value': 'material'}]},
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'made_of', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'themrole', 'value': 'material'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]}
],
'learn-14': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'learn-14-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'learn-14-2': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'learn-14-2-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'leave-51.2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'leave-51.2-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'lecture-37.11': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'lecture-37.11-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'lecture-37.11-1-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'lecture-37.11-2': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'let-64.2': [
                   { 'value': 'allow', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'light_emission-43.1': [
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'light'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'verbspecific', 'value': 'light'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'limit-76': [
                   { 'value': 'limit', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'causer'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'linger-53.1': [
                   { 'value': 'linger', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'linger-53.1-1': [
                   { 'value': 'delay', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'lodge-46': [
                   { 'bool': '!', 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'long-32.2': [
                   { 'value': 'desire', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'long-32.2-1': [
                   { 'value': 'desire', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'long-32.2-2': [
                   { 'value': 'desire', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'lure-59.3': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'predicate'}]},
                   { 'value': 'attract', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'manner_speaking-37.3': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_manner'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'marry-36.2': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]}
],
'marvel-31.3': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'masquerade-29.6': [
                   { 'value': 'masquerade', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'masquerade-29.6-1': [
                   { 'value': 'masquerade', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'masquerade-29.6-2': [
                   { 'value': 'masquerade', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'matter-91': [
                   { 'value': 'emotional_state', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'emotion'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'meander-47.7': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'has_configuration', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_configuration'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'meander-47.7-1': [
                   { 'value': 'has_configuration', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_configuration'}]}
],
'meet-36.3': [
                    { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]}
],
'meet-36.3-1': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]}
],
'meet-36.3-2': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'conflict', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]}
],
'mine-10.9': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'mix-22.1': [       { 'bool': '!', 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]}
],
'mix-22.1-1': [
                   { 'bool': '!', 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]}
],
'mix-22.1-1-1': [
                   { 'bool': '!', 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]}
],
'mix-22.1-2': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'mix-22.1-2-1': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'modes_of_being_with_motion-47.3': [
                   { 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'multiply-108': [
                   { 'value': 'calculate', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'multiply-108-1': [
                   { 'value': 'calculate', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'multiply-108-2': [
                   { 'value': 'calculate', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'multiply-108-3': [
                   { 'value': 'calculate', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'murder-42.1': [
                   { 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'bool': '!', 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]}
],
'murder-42.1-1': [
                   { 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'bool': '!', 'value': 'alive', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'neglect-75.1': [
                   { 'value': 'neglect', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'neglect-75.1-1': [
                   { 'value': 'neglect', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'nonvehicle-51.4.2': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'ee2'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'ee2'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'nonvehicle-51.4.2-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]}
],
'nonverbal_expression-40.2': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_manner'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'obtain-13.5.2': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'obtain-13.5.2-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e5'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'cost', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'occur-48.3': [
                   { 'value': 'occur', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'occur-48.3-1': [
                   { 'value': 'occur', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'occur-48.3-2': [
                   { 'value': 'occur', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'orbit-51.9.2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'elliptical_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'axis'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'predspecific', 'value': 'initial_location'},
                                       {'type': 'predspecific', 'value': 'destination'}]}
],
'order-58.3': [
                   { 'value': 'require', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'order-58.3-1': [
                   { 'value': 'require', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'orphan-29.7': [
                   { 'bool': '!', 'value': 'designated', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'v_result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'designated', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'v_result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'other_cos-45.4': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]}
],
'other_cos-45.4-1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'overstate-37.12': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'predspecific', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'own-100.1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'pain-40.8.1': [
                   { 'value': 'experience', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'discomfort', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'patent-101': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'license', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'pay-68': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'predspecific', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'predspecific', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'},
                                       {'type': 'predspecific', 'value': 'recipient'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'predspecific', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'predspecific', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'predspecific', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e5'}]},
                   { 'value': 'cost', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'pay-68-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'asset'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e5'}]},
                   { 'value': 'cost', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'asset'}]}
],
'peer-30.3': [
                   { 'value': 'perceive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'pelt-17.2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'repeat_sequence', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'event', 'value': 'e5'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e4'}]}
],
'performance-26.7': [
                   { 'value': 'perform', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'performance-26.7-1': [
                   { 'bool': '!', 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'pit-10.7': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'verbspecific', 'value': 'v_theme'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'play-114.2': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'playful'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]}
],
'play-114.2-1': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'playful'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]}
],
'pocket-9.10': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'pred_specific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'pocket-9.10-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'pred_specific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'destination'}]}
],
'poison-42.2': [
                   { 'bool': '!', 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'harmed', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]}
],
'poke-19': [
                   { 'bool': '!', 'value': 'penetrating', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'verbspecific', 'value': 'movement'}]},
                   { 'value': 'penetrating', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'penetrating', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'penetrating', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'poke-19-1': [
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'verbspecific', 'value': 'movement'}]},
                   { 'bool': '!', 'value': 'penetrating', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'verbspecific', 'value': 'movement'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'penetrating', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'penetrating', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'repeated_sequence', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'poke-19-1-1': [
                   { 'bool': '!', 'value': 'penetrating', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'verbspecific', 'value': 'movement'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'pour-9.5': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'preparing-26.3': [  { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'preparing-26.3-1': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'material'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'preparing-26.3-2': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'price-54.4': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'value', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'value'}]}
],
'promise-37.13': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'bool': '!', 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'promote-102': [
                   { 'value': 'promote', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'pronounce-29.3.1': [
                   { 'value': 'characterize', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'prosecute-33.2': [
                   { 'value': 'charge', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'prosecute-33.2-1': [
                   { 'value': 'charge', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'declare', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'push-12': [
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'push-12-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'ee2'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'ee2'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'push-12-1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'ee2'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'ee2'}]},
                   { 'value': 'equals', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'put-9.1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'put-9.1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'put-9.1-2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'put_direction-9.4': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'value': 'direction', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'verbspecific', 'value': 'v_direction'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'put_spatial-9.2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_configuration', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_configuration'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'reach-51.8': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'goal'}]}
],
'rear-26.2.2': [
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'rear-26.2.2-1': [
                   { 'bool': '!', 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'take_care_of', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'}]},
                   { 'value': 'made_of', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'product'},
                                       {'type': 'themrole', 'value': 'material'}]}
],
'reciprocate-112': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'predicate'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'reciprocate-112-1': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'predicate'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'reflexive_appearance-48.1.2': [
                   { 'value': 'appear', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'refrain-69': [
                   { 'bool': '!', 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'register-54.1': [
                   { 'value': 'value', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'value'}]}
],
'register-54.1-1': [
                   { 'value': 'assess', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'value', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'value'}]},
                   { 'value': 'value', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'value'}]}
],
'register-54.1-1-1': [
                   { 'value': 'value', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'value'}]}
],
'rehearse-26.8': [
                   { 'value': 'perform', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'rehearse-26.8-1': [
                   { 'value': 'perform', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'reject-77.2': [
                   { 'bool': '!', 'value': 'approve', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'reject-77.2-1': [
                   { 'bool': '!', 'value': 'approve', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'relate-86.2': [
],
'relate-86.2-1': [
                   { 'value': 'relate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'relate-86.2-2': [
                   { 'value': 'relate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'}]}
],
'rely-70': [
                   { 'value': 'depend', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'remedy-45.7': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]}
],
'remedy-45.7-1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'result'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'remove-10.1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'render-29.90': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'render-29.90-1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'render-29.90-2': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'result'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'representation-110.1': [
                   { 'value': 'signify', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'context'}]}
],
'require-103': [
                   { 'value': 'necessitate', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'precondition'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'require-103-1': [
                   { 'value': 'require', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'precondition'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'require-103-2': [
                   { 'value': 'require', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'precondition'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'resign-10.11': [
                   { 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'bool': '!', 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'predspecific', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'resign-10.11-1': [
                   { 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'bool': '!', 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'resign-10.11-2': [
                   { 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'bool': '!', 'value': 'has_organization_role', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'respond-113': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'predicate'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'result-27.2': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'precondition'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'risk-94': [
                   { 'value': 'risk', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'risk-94-1': [
                   { 'value': 'risk', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'rob-10.6.4': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'constant', 'value': 'illegal'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'roll-51.3.1': [
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'rotate-51.9.1': [
                   { 'bool': '!', 'value': 'has_orientation', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_orientation'}]},
                   { 'value': 'rotational_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'},
                                       {'type': 'themrole', 'value': 'extent'}]},
                   { 'value': 'has_orientation', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_orientation'}]}
],
'rotate-51.9.1-1': [
                   { 'bool': '!', 'value': 'has_orientation', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_orientation'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'rotational_motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'},
                                       {'type': 'themrole', 'value': 'extent'}]},
                   { 'value': 'has_orientation', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_orientation'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'rummage-35.5': [
                   { 'value': 'search', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'rummage-35.5-1': [
                   { 'value': 'search', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'run-51.3.2': [
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'run-51.3.2-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'run-51.3.2-2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'run-51.3.2-2-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'rush-53.2': [
                   { 'value': 'rush', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'end', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'satisfy-55.7': [
                   { 'value': 'satisfy', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'instrument'}]}
],
'say-37.7': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'say-37.7-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'say-37.7-1-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'say-37.7-1-1-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'say-37.7-1-2': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'scribble-25.2': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'create_image', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'scribble-25.2-1': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'create_image', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'search-35.2': [
                   { 'value': 'search', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'see-30.1': [
                   { 'value': 'perceive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'see-30.1-1': [
                   { 'value': 'perceive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'see-30.1-1-1': [
                   { 'value': 'perceive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'see-30.1-1-1-1': [
                   { 'value': 'perceive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'seem-109': [
                   { 'value': 'seem', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'seem-109-1': [
                   { 'value': 'seem', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'seem-109-1-1': [
                   { 'value': 'seem', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'seem-109-1-1-1': [
                   { 'value': 'seem', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'send-11.1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'send-11.1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'separate-23.1': [
                   { 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'bool': '!', 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'separate-23.1-1': [
                   { 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'bool': '!', 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'separate-23.1-2': [
                   { 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'bool': '!', 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'settle-36.1.2': [
                   { 'value': 'agree', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'agree', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'settle-36.1.2-1': [
                   { 'value': 'agree', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'shake-22.3': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'shake-22.3-1': [
                   { 'bool': '!', 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'shake-22.3-1-1': [
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'bool': '!', 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'bool': '!', 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'mingled', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'material_integrity_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'shake-22.3-2': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'shake-22.3-2-1': [
                   { 'bool': '!', 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'together', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'sight-30.2': [
                   { 'value': 'perceive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'simple_dressing-41.3.1': [
],
'simple_dressing-41.3.1-1': [
                   { 'value': 'wear', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'simple_dressing-41.3.1-2': [
                   { 'bool': '!', 'value': 'wear', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'wear', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'slide-11.2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'slide-11.2-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'smell_emission-43.3': [
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'odor'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'odor'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'odor'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'snooze-40.4': [
                   { 'value': 'body_process', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'sleep', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'snooze-40.4-1': [
                   { 'value': 'sleep', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'body_process', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'constant', 'value': 'quality'}]}
],
'sound_emission-43.2': [
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'sound'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'verbspecific', 'value': 'sound'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'sound'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'event', 'value': 'e1'}]}
],
'sound_existence-47.4': [
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'spank-18.3': [
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'movement'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'constant', 'value': 'forceful'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'movement'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'constant', 'value': 'forceful'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'spatial_configuration-47.6': [
                   { 'value': 'has_configuration', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_configuration'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'spatial_configuration-47.6-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'bool': '!', 'value': 'has_configuration', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_configuration'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'intrinsic_motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'value': 'has_configuration', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_configuration'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'spend_time-104': [
                   { 'value': 'spend', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'duration'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'event', 'value': 'e'}]},
                   { 'value': 'characterize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'}]},
                   { 'value': 'masquerade', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'split-23.2': [
                   { 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'bool': '!', 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]}
],
'spray-9.7': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'spray-9.7-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'spray-9.7-1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'spray-9.7-2': [
],
'stalk-35.3': [
                   { 'value': 'search', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'steal-10.5': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'illegal'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'steal-10.5-1': [
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'transfer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'constant', 'value': 'illegal'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_possession', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'benefit', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'beneficiary'}]}
],
'stimulate-59.4': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'predicate'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'stimulus_subject-30.4': [
                   { 'value': 'perceive', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'stop-55.4': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'causer'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'end', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'stop-55.4-1': [
                   { 'value': 'end', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'stop-55.4-1-1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'end', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'subjugate-42.3': [
                   { 'bool': '!', 'value': 'subjugated', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'subjugated', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]}
],
'subordinate-95.2.1': [
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'substance_emission-43.4': [
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'substance_emission-43.4-1': [
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee1'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'substance_emission-43.4-1-1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'emit', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'source'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'event', 'value': 'e1'}]}
],
'substitute-13.6.2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'co_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'co_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'ee3'}]}
],
'substitute-13.6.2-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'co_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'co_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'co_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'co_theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'ee3'}]}
],
'succeed-74': [
],
'succeed-74-1': [
                   { 'value': 'successful_in', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'succeed-74-1-1': [
                   { 'value': 'successful_in', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'succeed-74-2': [
                   { 'value': 'successful_in', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'succeed-74-3': [
                   { 'bool': '!', 'value': 'successful_in', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'succeed-74-3-1': [
                   { 'bool': '!', 'value': 'successful_in', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'succeed-74-3-1-1': [
                   { 'bool': '!', 'value': 'successful_in', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'suffocate-40.7': [
                   { 'bool': '!', 'value': 'suffocated', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'suffocated', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'bool': '!', 'value': 'suffocated', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'suffocate', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'supervision-95.2.2': [
                   { 'value': 'authority_relationship', 'args': [
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'}]}
],
'support-15.3': [
                   { 'value': 'support', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'support-15.3-1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'support', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'suspect-81': [
                   { 'value': 'suspect', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'sustain-55.6': [
                   { 'value': 'continue', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]}
],
'sustain-55.6-1': [
                   { 'value': 'continue', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'property', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'swarm-47.5.1': [
],
'swarm-47.5.1-1': [
                   { 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'swarm-47.5.1-2': [
                   { 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'swarm-47.5.1-2-1': [
                   { 'value': 'exist', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'swat-18.2': [
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'constant', 'value': 'movement'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'constant', 'value': 'forceful'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'constant', 'value': 'movement'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'constant', 'value': 'forceful'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'constant', 'value': 'movement'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'constant', 'value': 'movement'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'location'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'location'},
                                       {'type': 'themrole', 'value': 'patient'}]}
],
'talk-37.5': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'co_agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'co_topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'co_topic'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e4'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_topic'}]},
                   { 'value': 'repeated_sequence', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'event', 'value': 'e4'}]}
],
'tape-22.4': [
                   { 'bool': '!', 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'instrument'}]},
                   { 'value': 'attached', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'co_patient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'tell-37.2': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]}
],
'terminus-47.9': [
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'throw-17.1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e4'}]}
],
'throw-17.1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'overlaps', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e4'}]}
],
'throw-17.1-1-1': [
                   { 'bool': '!', 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'exert_force', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'causer'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'tingle-40.8.2': [
                   { 'value': 'discomfort', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'patient'}]},
                   { 'value': 'body_sensation', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'in_reaction_to', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'touch-20': [
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'experiencer'}]},
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'touch-20-1': [
                   { 'bool': '!', 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'instrument'}]},
                   { 'value': 'contact', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'instrument'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'experiencer'}]}
],
'transcribe-25.4': [
                   { 'bool': '!', 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'create_image', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'be', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'transfer_mesg-37.1.1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'transfer_mesg-37.1.1-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'transfer_mesg-37.1.1-1-1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'topic'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'topic'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'trick-59.2': [
                   { 'value': 'act', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'predicate'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'constant', 'value': 'deceptive'},
                                       {'type': 'themrole', 'value': 'agent'}]}
],
'trifle-105.3': [
                   { 'value': 'social_interaction', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'try-61.1': [
                   { 'value': 'attempt', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'turn-26.6.1': [
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'initial_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'opposition', 'args': [
                                       {'type': 'themrole', 'value': 'initial_state'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'turn-26.6.1-1': [
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'initial_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'opposition', 'args': [
                                       {'type': 'themrole', 'value': 'initial_state'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'urge-58.1': [
                   { 'value': 'urge', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'urge-58.1-1': [
                   { 'value': 'urge', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'urge-58.1-1-1': [
                   { 'value': 'urge', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'use-105.1': [
                   { 'value': 'use', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'predicate'}]}
],
'vehicle-51.4.1': [
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'vehicle-51.4.1-1': [
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'vehicle_path-51.4.3': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'ee3'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]}
],
'void-106': [
                   { 'bool': '!', 'value': 'voided', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'voided', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_final_state'}]}
],
'volunteer-95.4': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'designated', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'designated', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'volunteer-95.4-1': [
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'event', 'value': 'e1'}]},
                   { 'value': 'designated', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'has_property', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'attribute'}]}
],
'waltz-51.5': [
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_manner'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_manner'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'verbspecific', 'value': 'v_manner'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee4'},
                                       {'type': 'event', 'value': 'e3'}]},
                   { 'value': 'co_temporal', 'args': [
                                       {'type': 'event', 'value': 'ee5'},
                                       {'type': 'event', 'value': 'ee4'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e6'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e7'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e8'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'want-32.1': [
                   { 'value': 'desire', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'want-32.1-1': [
                   { 'value': 'desire', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'want-32.1-1-1': [
                   { 'value': 'desire', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'pivot'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'weather-57': [
                   { 'value': 'weather', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'verbspecific', 'value': 'weather_type'},
                                       {'type': 'themrole', 'value': 'theme'}]}
],
'weekend-56': [
                   { 'value': 'location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'location'}]}
],
'wink-40.3.1': [
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'bool': '!', 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'transfer_info', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'recipient'}]},
                   { 'value': 'body_motion', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'has_position', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'verbspecific', 'value': 'v_position'}]},
                   { 'value': 'has_information', 'args': [
                                       {'type': 'event', 'value': 'e3'},
                                       {'type': 'themrole', 'value': 'recipient'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'part_of', 'args': [
                                       {'type': 'themrole', 'value': 'patient'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee2'},
                                       {'type': 'event', 'value': 'e3'}]}
],
'wipe_instr-10.4.2': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_instrument'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]},
                   { 'value': 'has_state', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'initial_location'},
                                       {'type': 'themrole', 'value': 'result'}]}
],
'wipe_instr-10.4.2-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'utilize', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_instrument'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'initial_location'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'wipe_manner-10.4.1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'e2'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_manner'}]},
                   { 'value': 'motion', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'predspecific', 'value': 'trajectory'}]},
                   { 'bool': '!', 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e4'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'destination'}]},
                   { 'value': 'causer', 'args': [
                                       {'type': 'event', 'value': 'ee3'},
                                       {'type': 'event', 'value': 'e2'}]}
],
'wipe_manner-10.4.1-1': [
                   { 'value': 'has_location', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'theme'},
                                       {'type': 'themrole', 'value': 'source'}]},
                   { 'value': 'do', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'}]},
                   { 'value': 'manner', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'verbspecific', 'value': 'v_manner'}]}
],
'wish-62': [
                   { 'value': 'desire', 'args': [
                                       {'type': 'event', 'value': 'e'},
                                       {'type': 'themrole', 'value': 'experiencer'},
                                       {'type': 'themrole', 'value': 'stimulus'}]}
],
'withdraw-82': [ 
                   { 'value': 'withdraw', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'withdraw-82-1': [
                   { 'value': 'withdraw', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'withdraw-82-2': [
                   { 'value': 'withdraw', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'withdraw-82-3': [
                   { 'value': 'withdraw', 'args': [
                                       {'type': 'event', 'value': 'e1'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'source'}]}
],
'work-73.2': [
                   { 'value': 'work', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'theme'}]},
                   { 'value': 'cooperate', 'args': [
                                       {'type': 'event', 'value': 'ee'},
                                       {'type': 'themrole', 'value': 'agent'},
                                       {'type': 'themrole', 'value': 'co_agent'},
                                       {'type': 'themrole', 'value': 'theme'}]}
]}

