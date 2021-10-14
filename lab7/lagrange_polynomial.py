from numpy import *
from math import *
import matplotlib.pyplot as plt

# lab 7 variant 19

x = array([-4, -1, 1, 2])
y = array([-6, 3, -11, -6])

def lagr (k):
    l = 0
    for i in range (len(y)):
        p = 1
        for j in range (len(x)):
            if j != i:
                p *= (k - x[j])/(x[i]-x[j])
        l += y[i]*p
    return l

vars = [-3, -2, -0.5, 2.5]
for v in vars:
    print(f'x = {v}, f(x) = {lagr(v)}')

k = linspace(x[0], x[-1], 100)
k2 = lagr(k)
plt.plot(k, k2, 'c2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Variant 19')
plt.legend(['Lagrange polynomial'], loc = 'upper right')
plt.grid()
plt.show()

