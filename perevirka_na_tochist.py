from math import *;

def accuracy(exact1, approx1, exact2, approx2):

    dx1 = abs(approx1-exact1)
    dx2 = abs(approx2-exact2)
    sx1 = abs(dx1/exact1)
    sx2 = abs(dx2/exact2)

    if (sx1<sx2):
        print('The first equality is more accurate')
    elif (sx1==sx2):
        print('The equalities are of the same accuracy')
    else:
        print('The second equality is more accurate')

accuracy(sqrt(44), 6.63, 19/41, 0.463)