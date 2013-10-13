# Memoize decorator - a decorator that caches expensive computations
# Shamelessly copied from https://wiki.pthon.org/moin/PythonDecoratorLibrary

import collections


class memoized(object):
    '''Decorator that caches the return value of a function when it is called.
       If called later with the same arguments the cached value is returned
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # if args are not hashable forget trying to cache it,
            # just call the function normally
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
