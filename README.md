# Count verbs in the names of Python functions.

Language: **python**

## How to use it

Take any path to the python library `path`. 

	path =  r'c:\Program Files (x86)\Anaconda2\Lib\site-packages\sklearn'

After that you can do the following:

### Count top verbs in the names of functions

	get_top_verbs_in_path(path)

### Count top functions sorted by frequency of their using

	get_top_functions_names_in_path(d)

### Example of usage

Code:

	dirs = [
	        r'c:\Program Files (x86)\Anaconda2\Lib\site-packages\sklearn',
	        ]
	for d in dirs:
	    verbs = get_top_verbs_in_path(d)
	    print(f'get_top_verbs_in_path: {verbs}')
	
	    names = get_top_functions_names_in_path(d)
	    print(f'get_top_functions_names_in_path: {names}')

Answer:

	get_top_verbs_in_path: [('get', 98), ('make', 68), ('precomputed', 20), ('randomized', 17), ('weighted', 9), ('squared', 8), ('balanced', 8), ('paired', 8), ('stratified', 8), ('initialize', 7)]
	
	get_top_functions_names_in_path: [('fit', 177), ('predict', 69), ('transform', 58), ('predict_proba', 26), ('score', 25), ('fit_transform', 25), ('decision_function', 22), ('inverse_transform', 22), ('partial_fit', 21), ('configuration', 17)]


# Useful links

## The same work made by other people:

* https://github.com/tonkytonky/otus_lecture_1/blob/master/count_function_verbs.py

## NLTK

* https://www.nltk.org/book/ch05.html
* [With russian language](https://www.nltk.org/_modules/nltk/tag.html)

## Python
* https://realpython.com/python-f-strings/

## Different
* [Full course: Web-разработчик на Python](https://otus.ru/lessons/webpython/)


