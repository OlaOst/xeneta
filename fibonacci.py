# Fibonacci functions

from decorator import memoized
from math import sqrt


def trivialFib(n):
    '''Trivial fibonacci implementation, complexity O(2^n).
       Starts getting slow with n>30
    '''
    if n <= 1:
        return n
    else:
        return trivialFib(n-1) + trivialFib(n-2)


@memoized
def memoizedTrivialFib(n):
    '''Memoized trivial fibonacci. Same complexity as trivialFib, but O(1) on
       subsequent calls with same parameters
       (depending on the lookup in memoized)
    '''
    return trivialFib(n)


@memoized
def memoizedFib(n):
    '''Proper memoized fibonacci. Complexity probably O(n log n) since lots of
       similar recursive calls will be memoized
    '''
    if n <= 1:
        return n
    else:
        return memoizedFib(n-1) + memoizedFib(n-2)


def instaFib(n):
    '''Closed form, complexity O(1) but gives approximate results on large
       numbers because of float number inaccuracies
    '''
    phi = (1 + sqrt(5)) / 2
    return int((phi**n - (-1/phi)**n) / sqrt(5))


def loopyFib(n):
    '''A fibonacci using a loop instead of recursion. Complexity O(n)'''
    counter, a, b = 0, 0, 1

    while counter < n:
        counter, a, b = counter+1, b, a + b

    return a


print "The 10th fibonacci number is " + str(trivialFib(10 - 1))
print "The 100th fibonacci number is " + str(memoizedFib(100 - 1))
print "The 1200th fibonacci number is " + str(loopyFib(1200 - 1))

# TODO: a recursive fibonacci that gives correct results for n > 1200 without
# smashing the stack or taking too much time
