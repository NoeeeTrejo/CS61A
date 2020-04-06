def twenty_nineteen():
    """Come up with the most creative expression that evaluates to 2019,
    using only numbers and the +, *, and - operators.

    >>> twenty_nineteen()
    2019
    """
    expression = int(((e-349/500) * (10*10*10) - (2-e) - (2 + 11029/100000000) + (1-0.9999999975041) ))
    print(expression)
from math import e

twenty_nineteen()
