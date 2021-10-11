import math

def f(x):
        return 9*x**4 + 8*x**3 + 1.5*x**2 + 2*x - 10

def f_def (x):
        return 108*x**2 + 48*x + 3

def horda (a, b, e):

    if f(a) * f_def (a) > 0:
        x0 = a
        xi = b

    else:
        x0 = b
        xi = a

    x_prev = x0 + e
    i = 0

    while abs (xi-x_prev) >= e and i < 10:
        xi -= f(xi) * (xi-x_prev) / (f(xi)-f(x_prev))
        x_prev = xi
        print (xi)
        i += 1

    return xi

horda(-5, -3/2, 0.0001)