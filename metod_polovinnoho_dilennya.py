import functools
import math

def f(x):
    return 9*x**4 + 8*x**3 + 1.5*x**2 + 2*x - 10

def half (a, b, e):

    global x

    if (f(a) * f(( a + b) / 2) < 0):
        b = ( a + b ) / 2

    else:
        a = (a + b) / 2

    if(abs(b - a) <= e):
        x = (a + b) / 2

    else:
        half (a, b, e)

    return x

half=functools.lru_cache(half)
print(half (-5, -3/2, 0.0001))