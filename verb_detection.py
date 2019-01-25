from nltk import pos_tag

import nltk

try:
    pos_tag(['hello'])
except Exception as er:
    print('nltk: download averaged_perceptron_tagger')
    nltk.download('averaged_perceptron_tagger')

def is_verb(word):
    '''
    Check if our word is Verb or no
    '''
    if not word:
        return False
    pos_info = pos_tag([word])
    #print('             ', pos_info)
    return pos_info[0][1] in ['VB', 'VBN']

def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


