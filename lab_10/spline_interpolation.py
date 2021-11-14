import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
import sympy as sp
from matplotlib import style

x = [0, 0.2, 0.5, 0.9, 1.5]
y = [1.75, 2.68, 1.24, 0.72, 1.35]

#x = [0, 1.4, 2.3, 3.3, 4.5]
#y = [1, 1.155, 0.079, -1.145, -1.188]

x_i = sp.symbols('x_i')

h = []
m = []
k = []
alpha = [0, 0]
beta = [0, 0]
a = y
b = [0]
c = [0]
d = [0]

ys = []

def spline_fun(xk):

    for i in range(len(x)):
        h_i = x[i] - x[i-1]
        h.append(h_i)
    #print(h)

    for i in range(len(h)):
        m_i = 2 * (h[i-1] + h[i])
        m.append(m_i)
    #print(m)

    for i in range(len(h)):
        k_i = 3 * ( ((y[i] - y[i-1]) / h[i]) - ((y[i-1] - y[i-2]) / h[i-1]) )
        k.append(k_i)
    #print(k)

    for i in range (2, len(h)):
        alpha_i = (k[i] - h[i-1]*alpha[i-1]) / (m[i] - h[i-1]*beta[i-1])
        alpha.append(alpha_i)
        beta_i = h[i] / (m[i] - h[i-1]*beta[i-1])
        beta.append(beta_i)
    #print(alpha)
    #print(beta)

    for i in range (1, len(alpha)):
        c_i = alpha[-i] - beta[-i]*c[-i]
        c.insert(0, c_i)
    #print(c)

    i = len(c) - 1
    while i >= 0:
        d_i = (c[i]-c[i-1]) / (3 * h[i])
        d.insert(0, d_i)
        i-=1
    #print(d)

    i = len(c) - 1
    while i >= 0:
        b_i = ((y[i] - y[i-1]) / h[i]) - (((c[i] + 2*c[i-1]) * h[i] )/ 3)
        b.insert(0, b_i)
        i -= 1
    #print(b)

    print('\nThe spline:\n')
    for i in range(len(c)-1):
        s_i = a[i] + b[i+1]*(x_i - x[i]) + c[i]*((x_i-x[i])**2) + d[i+1]*((x_i-x[i])**3)
        print(s_i)

    def spline(i, x_j):
        s_ij = a[i] + b[i+1]*(x_j - x[i]) + c[i]*((x_j-x[i])**2) + d[i+1]*((x_j-x[i])**3)
        return s_ij

    print('\n\nValues of the spline at given points:\n')
    for i in range(len(x)-1):
        print(spline(i, x[i]))
    print('\n')

    for i in range(len(xk)):
        if (xk[i] >= x[0]) & (xk[i] < x[1]):
            yi = spline(0, xk[i] )

        elif (xk[i] >= x[1]) & (xk[i] < x[2]):
            yi = spline(1, xk[i] )
            
        elif (xk[i] >= x[2]) & (xk[i] < x[3]):
            yi = spline(2, xk[i] )
  
        elif (xk[i] >= x[3]) & (xk[i] < x[4]):
            yi = spline(3, xk[i] )

        ys.append(yi)

    return ys

xs = linspace(0, 1.5, 100)
xsl = xs.tolist()
spl = spline_fun(xsl)

spl1 = UnivariateSpline(x, y)

style.use('seaborn-whitegrid')

plt.plot( xs, spl, color = '#316879')
plt.plot(xs, spl1(xs), '--', color = '#7fe7dc')
plt.plot(x, y, '*', color = '#f47a60' )

plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline plot')
plt.legend(['my spline', 'UnivariateSpline', 'input data'])

plt.show()









