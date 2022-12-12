import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a, b, c = 1 / 4, 1, 5.5


def ressler(state, t):
    x, y, z = state
    return [- y - z,
            x + a * y,
            b + z * (x - c)]


t = np.linspace(0, 10, 1000)
init_cond = [1, 1, 1]
[x, y, z] = odeint(ressler, init_cond, t, full_output=False).T
plt.plot(x, z, color='black', linestyle=' ', marker='.',
         markersize=2)
plt.xlabel('x')
plt.ylabel('z')
plt.grid(True)
plt.title("Проекция траектории Рёсслера на плоскость xz")
plt.show()
