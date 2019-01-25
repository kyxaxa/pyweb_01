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

def read_file(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as attempt_handler:
        main_file_content = attempt_handler.read()
    return main_file_content

def get_trees(path, with_filenames=False, with_file_content=False, extension='.py', encoding='utf-8'):
    '''
        searching for .py files
    '''
    #encoding = 'cp1251'
    filenames = []
    trees = []

    ### search filenames with good extension
    for dirname, dirs, files in os.walk(path, topdown=True):
        #print(f'path {path}, dirname {dirname}, dirs {dirs}, files {files}')
        filenames.append( [
                os.path.join(dirname, file)
                for file in files if file.endswith(extension)
                ]
                )
    filenames = flat(filenames)

    print(f'total %s files with extension {extension}' % len(filenames))

    for filename in filenames:
        main_file_content = read_file(filename, encoding)

        try:
            tree = ast.parse(main_file_content)
        except Exception as e:
            print('error', e)
            tree = None
            continue

        if with_filenames:
            if with_file_content:
                trees.append((filename, main_file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)
    print(f'{len(trees)} trees generated')
    return trees


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_top_verbs_in_path(path, top_size=10):
    trees = [t for t in get_trees(path) if t]
    fncs = [f for f
            in flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in trees])
            if not (f.startswith('__') and f.endswith('__'))]
    print(f'{len(fncs)} functions extracted')
    print(fncs[:10])

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

    # test is_verb()
    t = 1
    t = 0
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
            print(f'{w} is_verb %s' % (w, is_verb(w)))

    # test get_trees()
    t = 0
    t = 1
    if t:
        dirs = [
                #r'unknown',
                #r'.git',
                #r'c:\!code\PyWeb\01\dz1\.git',
                #r'c:\Program Files (x86)\Anaconda2\Lib\site-packages\modules',
                r'c:\Program Files (x86)\Anaconda2\Lib\site-packages\sklearn',
                ]
        for d in dirs:
            t = 0
            if t:
                trees = get_trees(d)
                print('-'*20, f'directory {d}')
                #print(f'     trees {trees}')

            t = 0
            t = 1
            if t:
                verbs = get_top_verbs_in_path(d)
                print(f'get_top_verbs_in_path: {verbs}')

            t = 1
            if t:
                names = get_top_functions_names_in_path(d)
                print(f'get_top_functions_names_in_path: {names}')

    os._exit(0)


if __name__ == '__main__':

    t = 1
    t = 0
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
        r'c:\Program Files (x86)\Anaconda2\Lib\site-packages\sklearn',
    ]
    for project in projects:
        #path = os.path.join('.', project)
        wds += get_top_verbs_in_path(project)

    top_size = 200
    print(f'total {len(wds)} words, {len(set(wds))} unique')
    for word, occurence in collections.Counter(wds).most_common(top_size):
        print(word, occurence)
