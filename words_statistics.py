import ast

from base_functions import *
from work_with_files import *
from verb_detection import *


def get_astTrees_from_filenames(filenames=[], encoding='utf-8'):
    trees = []
    for filename in filenames:
        main_file_content = read_file(filename, encoding)

        try:
            tree = ast.parse(main_file_content)
        except Exception as e:
            print('error', e)
            continue

        trees.append(tree)
    return trees


def get_trees(
        path,
        with_filenames=False,
        with_file_content=False,
        extension='.py',
        encoding='utf-8',
        ):
    '''
        searching for .py files
    '''
    #encoding = 'cp1251'

    filenames = get_files_from_directory(path, extension=extension)

    print(f'total %s files with extension {extension}' % len(filenames))

    ast_trees = get_astTrees_from_filenames(filenames, encoding=encoding)

    trees = []
    for tree in ast_trees:
        if with_filenames:
            if with_file_content:
                trees.append((filename, main_file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)
    print(f'{len(trees)} trees generated')
    return trees


def get_top_verbs_in_path(path, top_size=10):
    trees = [t for t in get_trees(path) if t]
    fncs = [f for f
            in flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in trees])
            if not (f.startswith('__') and f.endswith('__'))]
    print(f'{len(fncs)} functions extracted')
    print(fncs[:10])

    verbs = flat([get_verbs_from_function_name(function_name) for function_name in fncs])
    return get_top_of_list(verbs, top_size)


def get_top_functions_names_in_path(path, top_size=10):
    t = get_trees(path)
    nms = [
        f for f
        in flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in t])
        if not (f.startswith('__') and f.endswith('__'))]
    return get_top_of_list(nms, top_size)


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
    for word, occurence in get_top_of_list(wds, top_size):
        print(word, occurence)
