import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt


def load_data(filename):
    return loadtxt(filename, usecols=(0,1), unpack=True)

filename = 'force_data.tsv'
reading, mass = load_data(filename)

def force(x, a, b, c, d):
    return a * np.exp(b * x + c) + d

params, _ = optimize.curve_fit(force, mass, reading, maxfev=5000)
a, b, c, d = params

x_fit = np.linspace(min(mass), max(mass)+ 1, 100)
y_fit = force(x_fit, a, b, c, d)

plt.plot(mass, reading, 'ro', label="Data")
plt.plot(x_fit, y_fit, 'b-', label=f"$y = {a:.4f} e^{{{b:.4f} x + {c:.4f}}} + {d:.4f}$")
plt.xlabel('Sensor Reading')
plt.ylabel('Mass (g)')
plt.title('Force Calibration')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

print(f'a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, d = {d:.4f}')
