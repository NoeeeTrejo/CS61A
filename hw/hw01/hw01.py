""" Homework 1: Control """

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = a - b
    else:
        f = a + b

    return f

a_plus_abs_b(2,3)
a_plus_abs_b(2,-3)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return pow(max(a,b), 2) + pow(max(b,c),2)
two_of_three(1,2,3)
two_of_three(5,3,1)
two_of_three(10,2,8)
two_of_three(5,5,5)

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    i = 1
    maximum = 0
    while i < n:

        if n % i == 0:
            maximum = i
        i += 1
    return(maximum)


largest_factor(15)
largest_factor(80)
largest_factor(13)

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()


def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return(False)


def t():
    "*** YOUR CODE HERE ***"
    print(1)
    return


def f():
    "*** YOUR CODE HERE ***"
    print(2)
    return


if_function(True, 2, 3)
if_function(False, 2, 3)
if_function(3 == 2, 3 + 2, 3 - 2)
if_function(3>2, 3+2, 3-2)


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    length = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n/2
            print(int(n))
            length = length + 1


        else:
            n = n * 3 + 1
            print(int(n))
            length = length + 1
    return(length)

a = hailstone(10)
