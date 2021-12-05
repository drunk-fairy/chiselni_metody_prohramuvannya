from numpy import *
import math
import matplotlib.pyplot as plt
from matplotlib import style

def f1(x, y):
    return x + math.cos(y/sqrt(5))

def f2(x, y):
    return x + math.sin(y/3)

#def f_2(x, y):
    #return math.sin(x) - math.cos(y)

xarr1 = []
yarr1 = []
xarr2 = []
yarr2 = []


def euler(f, x, y, a, b, h):

    xi = x
    yi = y
    for i in range(0, round((b-a)/h)+1):
        xarr1.append(xi)
        yarr1.append(yi)
        xi = xi + h
        yi1 = yi + h * f (xi, yi)
        yi = yi1

    print("\n-----Euler's method-----\n")
    print("xi: \n", xarr1)
    print('\n')
    print("yi: \n", yarr1)
    print('\n')

    return 0


def euler_cauchy(f, x, y, a, b, h):
    xi = x
    yi = y
    for i in range(0, round((b-a)/h)+1):
        xarr2.append(xi)
        yarr2.append(yi)
        xi1 = xi + h
        yi1 = yi + h/2 * ( f(xi, yi) + f(xi1, yi + (h * f(xi, yi))) )
        xi = xi1
        yi = yi1

    print("\n-----Euler-Cauchy's method-----\n")
    print("xi: \n", xarr2)
    print('\n')
    print("yi: \n", yarr2)
    print('\n\n')

    return 0


euler(f1, 1.8, 2.6, 1.8, 2.8, 0.1)
#euler(f_2, 0, 1, 0, 1, 0.2)
euler_cauchy(f2, 1.6, 4.6, 1.6, 2.6, 0.1)

style.use('seaborn-whitegrid')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Euler's and Euler-Cauchy's method")
plt.plot(xarr1, yarr1, 'r.-')
plt.plot(xarr2, yarr2, 'b.-')
plt.legend(["x + cos(y/sqrt(5)), Euler's method", "x + sin(y/3), Euler-Cauchy's method"])
plt.show()