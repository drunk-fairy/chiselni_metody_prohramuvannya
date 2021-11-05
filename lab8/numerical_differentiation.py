import numpy as np
import math

xarr = [2.4, 2.6, 2.8, 3.0, 3.2, 3.4]
yarr = [3.526, 3.782, 3.945, 4.043, 4.104, 4.155]

h = xarr[1] - xarr[0]

def y(yarr, k):

    arr = []

    for i in range(len(yarr)):
        arr.append(yarr[i]-yarr[i-1])

    arr.pop(0)

    if k == 1:
        return arr

    else:
        k-=1
        return y(arr, k)

yx1 = 1 / h * (y(yarr, 1)[0] - y(yarr, 2)[0]/2 +y(yarr, 3)[0]/3 - y(yarr, 4)[0]/4 + y(yarr,5)[0]/5)
yx2 = 1 / h**2 * (y(yarr, 2)[0] - y(yarr, 3)[0] + 11/12*y(yarr, 4)[0] - 5/6*y(yarr, 5)[0])

print('yx1 =', yx1)
print('yx2 =', yx2)
