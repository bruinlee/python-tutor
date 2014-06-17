#!/usr/bin/python

def print_max(x, y):
    '''prints the maximun of two numbers.
    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

help(print_max)
