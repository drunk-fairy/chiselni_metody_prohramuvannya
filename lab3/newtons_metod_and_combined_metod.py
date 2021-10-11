import functools

def d(x):
    return x**4-4*x-1
    #return 9*x**4 + 8*x**3 + 1.5*x**2 + 2*x - 10

def d1(x):    
    return 4*x**3 - 4
    #return 36*x**3+24*x**2+3*x+2

def d2(x):
    return 12*x**2
    #return 108*x**2 + 48*x + 3

#print(d(1))

def newt(a, b, e):

    f = d(b)
    f2 = d2(b)

    if (f*f2 > 0):
        x = b

    else:
        x = a

    def rec(x):

        f = d(x)
        f1 = d1(x)

        h = f/f1
        x = x - h

        if (abs(h) <= e):
            global x1
            x1 = x - f/f1

        else:
            rec(x)


        return x1

    rec = functools.lru_cache(rec)
    rec(x)

    return x1

print(newt(-5, 1, 0.0001))


def comb(a, b, e):

    while((b-a)>e):

        if (d1(a)*d2(a)>0):
            a1 = a - d(a)*(b - a) / (d(b)-d(a))
            b1 = b - d(b) / d1(b)

        else:
            
            a1 = a - d(a) / d1(a)
            b1 = b - d(b)*(b - a) / (d(b)-d(a))

        a = a1
        b = b1

    x = (a+b) / 2

    return x

print(comb(-5, 1, 0.0001))