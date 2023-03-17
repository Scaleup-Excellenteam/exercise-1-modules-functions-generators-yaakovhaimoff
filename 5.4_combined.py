from itertools import chain, zip_longest

def interleave(*iterables):
    if not iterables:
        return None
    yield from filter(None, chain.from_iterable(zip_longest(*iterables)))


our_generator = interleave('abc', [1, 2, 3], ('!', '@', '#'))
print(list(our_generator))
