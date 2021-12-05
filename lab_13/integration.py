from scipy import integrate
from numpy import *
import math


def f1(x):
    return 1/sqrt(2*x**2 + 1)

def f2(x):
    return math.log10(x+2) / x

def f3(x):
    return 1 / sqrt(x**2 + 2.3)


def rectleft(f1, a, b, n):

    h = (b-a)/n
    sum = 0

    for i in range(0, n):
        y = f1(a+i*h)
        sum = sum + y

    return h*sum


def rectright(f1, a, b, n):

    h = (b-a)/n
    sum = 0

    for i in range(1, n+1):
        y = f1(a+i*h)
        sum = sum + y

    return h*sum


def rectmid(f1, a, b, n):

    h = (b-a)/n
    sum = 0

    for i in range(0, n):
        y = f1(a + h/2 + (i*h))
        sum = sum + y

    return h*sum


def simpson(f2, a, b, n):

    h = (b-a)/n
    sum_p = 0
    sum_unp = 0
    sum_fl = 0

    for i in range (0, n+1):
        if (i==0) | (i==n):
            y = f2(a+i*h)
            sum_fl = sum_fl + y

    for i in range (0, n+1):
        if (i!=0) & (i!=n) & (i%2==1):
            y = f2(a+i*h)
            sum_unp = sum_unp + y

    for i in range (0, n+1):
        if (i!=0) & (i!=n) & (i%2==0):
            y = f2(a+i*h)
            sum_p = sum_p + y

    return h/3 * (sum_fl + 4*sum_unp + 2*sum_p)


def trapezoid(f3, a, b, n):

    h = (b-a)/n
    sum = 0.5 * (f3(a) + f3(b))
    
    for i in range(1, n):
        sum = sum + f3(a + i*h)

    return h*sum


print('\nleft rule: \n', rectleft(f1, 0.8, 1.6, 10))
print('\nright rule: \n', rectright(f1, 0.8, 1.6, 10))
print('\nmidpoint rule: \n', rectmid(f1, 0.8, 1.6, 10))
print("\nSimpson's method: \n", simpson(f2, 1.2, 2, 8))
print('\ntrapedoizal method: \n', trapezoid(f3, 0.32, 0.66, 20))

ch1, err = integrate.quad(f1, 0.8, 1.6)
ch2, err = integrate.quad(f2, 1.2, 2)
ch3, err = integrate.quad(f3, 0.32, 0.66)

print('\nCheck for Riemann sum: \n', ch1)
print("\nCheck for Simpson's method: \n", ch2)
print('\nCheck for trapedoizal method: \n', ch3)

print('\n')


