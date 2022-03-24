import itertools\

def cycle(iterator):
    return itertools.cycle('ABCD')

def cycle_naive(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D A B ...

    saved = []
    for element in iterable:
        yield element
        saved.append(element)

    while saved:
        for element in saved:
            yield element
