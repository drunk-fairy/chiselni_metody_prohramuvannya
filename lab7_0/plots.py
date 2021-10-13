from numpy import *
import matplotlib.pyplot as plt

# Example 1
plt.plot([1, 3, 2, 4])
plt.show()

# Example 2
def f(t):
    return t ** 2 * exp(-t ** 2)
t = linspace(0, 3, 51) # 51 точка між 0 та 3
y = f(t)
plt.plot(t, y)
plt.show()

# Example 3
t = linspace(0, 3, 51)
y = t ** 2 * exp(-t ** 2)
plt.plot(t, y, 'g--', label='t^2*exp(-t^2)')
plt.axis([0, 3, -0.05, 0.5]) # [xmin, xmax, ymin, ymax]
plt.xlabel('t') # позначення вісі абсцис
plt.ylabel('y') # позначення е вісі ординат
plt.title('My first normal plot') # назва графіка
plt.legend() # вставка легенди (тексту в label)
plt.show()

# Example 4
t = linspace(0, 3, 51)
y1 = t ** 2 * exp(-t ** 2)
y2 = t ** 4 * exp(-t ** 2)
y3 = t ** 6 * exp(-t ** 2)
plt.plot(t, y1, 'g^', # маркери із зелених трикутників
t, y2, 'b--', # синя штрихова
t, y3, 'ro-') # червоні круглі маркери
# з'єднані суцільною лінією
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plotting with markers')
plt.legend(['t^2*exp(-t^2)',
't^4*exp(-t^2)',
't^6*exp(-t^2)'], # список легенди
loc='upper left') # положення легенди
plt.show()


# Example 5
x = [5, 3, 7, 2, 4, 1]
plt.xticks(range(len(x)), ['a', 'b', 'c', 'd', 'e', 'f'])
plt.yticks(range(1, 8, 2))
plt.show()

# The task (var 1)
x = linspace(-2, 5, 100)
y = x * sin(5*x)
plt.plot(x, y, 'y*')
plt.xlabel('x')
plt.ylabel('y')
plt.title('My plot (variant 1)')
plt.legend(['y = x * sin(5*x)'], loc = 'lower left')
plt.grid()
plt.show()
