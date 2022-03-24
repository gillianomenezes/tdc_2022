import itertools

def filterfalse(predicate, iterator):
    return itertools.filterfalse(predicate, iterator)

def filterfalse_naive(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) -> 0 2 4 6 8 
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x