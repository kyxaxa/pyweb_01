import os

from base_functions import *

def read_file(filename='', encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as attempt_handler:
        main_file_content = attempt_handler.read()
    return main_file_content

def get_files_from_directory(path='', extension='.py'):
    '''
        get all files in directory
    '''
    filenames = []
    ### search filenames with good extension
    for dirname, dirs, files in os.walk(path, topdown=True):
        #print(f'path {path}, dirname {dirname}, dirs {dirs}, files {files}')
        filenames.append( [
                os.path.join(dirname, file)
                for file in files if file.endswith(extension)
                ]
                )
    filenames = flat(filenames)
    return filenames

