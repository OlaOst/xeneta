# Fibonacci functions

from decorator import memoized
from math import sqrt, floor

def trivialFib(n):
    if n <= 1:
        return n
    else:
        return trivialFib(n-1) + trivialFib(n-2)

@memoized
def memoizedTrivialFib(n):
    return trivialFib(n)

@memoized
def memoizedFib(n):
    if n <= 1:
        return n
    else:
        return memoizedFib(n-1) + memoizedFib(n-2)

def instaFib(n):
    phi = (1 + sqrt(5)) / 2
    return int((phi**n -(-1/phi)**n) / sqrt(5))
