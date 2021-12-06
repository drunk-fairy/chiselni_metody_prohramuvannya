import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import integrate

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]

time = np.linspace(0, 11, 12)

print('\nTime array: ')
print(time)

plt.plot(time, speed, '--', color = '#4dc49a')

f1 = interpolate.interp1d(time, speed, kind = 'cubic')
f2 = interpolate.interp1d(time, speed, kind = 'quadratic')
x1 = np.arange(0, 11, 0.0011)
y1 = f1(x1)
y2 = f2(x1)
plt.plot(x1, y1, '-', color = '#696eff')
plt.plot(x1, y2, '-', color = '#ff8a24')

plt.plot(time, speed, '.', color = '#ff0062')

plt.axis([0, 11, 0, 130])
plt.title('Speed vs time plot')
plt.xlabel('time')
plt.ylabel('speed')
plt.legend(["time/speed",
            "Cubic interpolatioin",
            "Quadratic interpolation",
            "Speed spots"])
plt.grid()

v1, err = integrate.quad(f1, time[0], time[-1])
v2, err = integrate.quad(f2, time[0], time[-1])

print('\nintegral of cubic interpolatioin: ')
print(v1)
print('\nintegral of quadratic interpolation: ')
print(v2)

print('\n')

plt.show()

