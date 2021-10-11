import math
from math import sin, cos
from scipy import optimize

x0 = 0.5
y0 = -0.2

def f1(y):
    return 1 - cos(y)/2

def f2(x):
    return sin(x + 1) - 1.2

def iterate (x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1

    while ((abs(xn1 - xn) >= e) & (abs(yn1 - yn) >= e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1

    print ('\n ~ Method of simple iteration ~\n')
    print (f'x1 = {xn} \ny1 = {yn} \nNumber of iterations: {n}\n')

iterate (x0, y0, 0.001)

def f(x):
    return sin(x[0]+1) - x[1] - 1.2, 2*x[0] + cos(x[1]) - 2

check = optimize.root(f, [0,0], method = 'hybr')

print (f'Check of the method: \n{check.x}\n')
