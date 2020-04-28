#!/usr/bin/env python3

def mulf(*vars):
    """Returns vars[0] * ...

    >>> mulf(1,2,3,4)
    24
    >>> mulf(1,2,3,4, "Z")
    'ZZZZZZZZZZZZZZZZZZZZZZZZ'
    """
    v = 1
    for i in vars:
        v *= i
    return v
