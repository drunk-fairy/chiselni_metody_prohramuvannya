from numpy import *
from math import *
#import copy
import matplotlib.pyplot as plt

# Avdeeva Serafima FIT 2-4 
# lab 9 variant 1

xarr = [1.415, 1.420, 1.425, 1.430, 1.435, 1.440, 1.445, 1.450, 1.455, 1.460]
yarr = [0.8885, 0.8895, 0.8906, 0.8916, 0.8926, 0.8936, 0.8947, 0.8956, 0.8966, 0.8976]

#xarr = [0, 0.2, 0.4, 0.6, 0.8, 1]
#yarr = [1.2715, 2.4652, 3.6443, 4.8095, 5.9614, 7.1005]

x1 = 1.416 
x2 = 1.456

#x1 = 0.1
#x2 = 0.9

h = xarr[1] - xarr[0]

q1 = (x1 - xarr[0]) / h
q2 = (x2 - xarr[-1]) / h

def y(yarr, k):

    arr = []

    for i in range(len(yarr)):
        arr.append(yarr[i] - yarr[i-1])

    arr.pop(0)

    if k == 1:
        return arr

    else:
        k -= 1
        return y(arr, k)

n1 = yarr[0] + q1 * y(yarr, 1)[0]
n2 = yarr[-1] + q2 * y(yarr, 1)[-2]

dod1 = []
dod2 = []

#d1 = copy.copy(q1)
#d2 = copy.copy(q2)

# I had a case when my code didn't work properly without copying.
# Here it seems to be unnecessary, but I left it in the comments
# just to be on the safe side

d1 = q1
d2 = q2

for i in range (len(xarr)):
    d1 = d1 * (q1 - i)
    d2 = d2 * (q2 + i)
    dod1.append(d1)
    dod2.append(d2)

for i, j, k in zip(range (len(xarr)-2), range(2, len(xarr)), range(len(xarr)-2, 0)):
    n1 = n1 + dod1[i] / factorial(j) * y(yarr, j)[0]
    n2 = n2 + dod2[i] / factorial(j) * y(yarr, j)[k]

print(n1)
print(n2)

plt.plot(xarr, yarr, '.-', color = '#008bd6')
plt.plot(x1, n1, 'o', color = '#2fff00')
plt.plot( x2, n2, 'o', color = '#ff0066')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation function plot')
plt.legend(['y = N(x)', 'f(x1)', 'f(x2)'])
plt.grid()
plt.show()

