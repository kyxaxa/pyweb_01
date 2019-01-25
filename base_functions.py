import collections

def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def get_top_of_list(verbs, top_size):
    return collections.Counter(verbs).most_common(top_size)


