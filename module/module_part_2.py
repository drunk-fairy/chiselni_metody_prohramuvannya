import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(t, state, alpha, beta):
    s, i, r = state
    return([-alpha*s*i, alpha*s*i - beta*i, beta*i])

s = 0.99
i = 0.007
r = 0.003

alpha = 0.5
beta = 0.3
t_span = (0, 25)

p = (alpha, beta)

sol = solve_ivp(f, t_span, (s, i, r), args = p, t_eval = np.linspace(0, 23, 25))

fig = plt.figure()
ax = fig.add_subplot()

ax.plot(sol.y[0, :], label = 'S(t)', color = '#ff367c')
ax.plot(sol.y[1, :], label = 'I(t)', color = '#7c36ff')
ax.plot(sol.y[2, :], label = 'R(t)', color = '#ffb536')

ax.set_title("SIR model")

plt.xlabel('time -->')
plt.legend()
plt.grid()
plt.show()

