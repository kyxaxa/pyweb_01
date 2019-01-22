import ast
import os
import collections

from nltk import pos_tag

import nltk

try:
    pos_tag(['hello'])
except Exception as er:
    print('nltk: download averaged_perceptron_tagger')
    nltk.download('averaged_perceptron_tagger')

Path = ''


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    '''
    Check if our word is Verb or no
    '''
    if not word:
        return False
    pos_info = pos_tag([word])
    #print('             ', pos_info)
    return pos_info[0][1] in ['VB', 'VBN']

def get_trees(_path, with_filenames=False, with_file_content=False):
    filenames = []
    trees = []
    path = Path
    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith('.py'):
                filenames.append(os.path.join(dirname, file))
                if len(filenames) == 100:
                    break
    print('total %s files' % len(filenames))
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None
        if with_filenames:
            if with_file_content:
                trees.append((filename, main_file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)
    print('trees generated')
    return trees


def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_all_words_in_path(path):
    trees = [t for t in get_trees(path) if t]
    function_names = [
            f for f in flat([get_all_names(t) for t in trees])
            if not (f.startswith('__') and f.endswith('__'))
            ]

    def split_snake_case_name_to_words(name):
        return [n for n in name.split('_') if n]

    return flat([
        split_snake_case_name_to_words(function_name)
        for function_name in function_names
        ])


def get_top_verbs_in_path(path, top_size=10):
    global Path
    Path = path
    trees = [t for t in get_trees(None) if t]
    fncs = [f for f
            in flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in trees])
            if not (f.startswith('__') and f.endswith('__'))]
    print('functions extracted')
    verbs = flat([get_verbs_from_function_name(function_name) for function_name in fncs])
    return collections.Counter(verbs).most_common(top_size)


def get_top_functions_names_in_path(path, top_size=10):
    t = get_trees(path)
    nms = [
        f for f
        in flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in t])
        if not (f.startswith('__') and f.endswith('__'))]
    return collections.Counter(nms).most_common(top_size)


def test_functions():
    '''
        test unknown functions
    '''

    # test flat()
    t = 1
    t = 0
    if t:
        print(1, sum([[1, 2]], [3, 4]))
        #print(2, sum([1, 2], [3]))
        print(3, flat([(1, 2), (3, 4)]))

    # test is_verb
    t = 0
    t = 1
    if t:
        words = [
                'hello',
                'like',
                'love',
                'fetch',

                'refuse',
                'permit',

                'obtain',
                'liked',
                'valued',
                ]
        for w in words:
            print('%s is_verb %s' % (w, is_verb(w)))

    os._exit(0)


if __name__ == '__main__':

    t = 1
    if t:
        test_functions()

    wds = []
    projects = [
        'django',
        'flask',
        'pyramid',
        'reddit',
        'requests',
        'sqlalchemy',
    ]
    for project in projects:
        path = os.path.join('.', project)
        wds += get_top_verbs_in_path(path)

    top_size = 200
    print('total %s words, %s unique' % (len(wds), len(set(wds))))
    for word, occurence in collections.Counter(wds).most_common(top_size):
        print(word, occurence)
