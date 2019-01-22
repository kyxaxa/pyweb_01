# First homework for course PyWeb

Reusable library for everybody :)


## Example of usage:

```
dirs = [
        r'c:\Program Files (x86)\Anaconda2\Lib\site-packages\sklearn',
        ]
for d in dirs:
    verbs = get_top_verbs_in_path(d)
    print(f'get_top_verbs_in_path: {verbs}')

    names = get_top_functions_names_in_path(d)
    print(f'get_top_functions_names_in_path: {names}')
```

Answer:
```
get_top_verbs_in_path: [('get', 98), ('make', 68), ('precomputed', 20), ('randomized', 17), ('weighted', 9), ('squared', 8), ('balanced', 8), ('paired', 8), ('stratified', 8), ('initialize', 7)]

get_top_functions_names_in_path: [('fit', 177), ('predict', 69), ('transform', 58), ('predict_proba', 26), ('score', 25), ('fit_transform', 25), ('decision_function', 22), ('inverse_transform', 22), ('partial_fit', 21), ('configuration', 17)]
```

# Useful links

## NLTK

* https://www.nltk.org/book/ch05.html
* [With russian language](https://www.nltk.org/_modules/nltk/tag.html)

## Python
* https://realpython.com/python-f-strings/
