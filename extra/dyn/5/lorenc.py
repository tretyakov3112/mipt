import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

s, r, b = 10, 28, 8 / 3


def lorenc(state, t):
    x, y, z = state
    return [s * (y - x),
            -y + (r - z) * x,
            -b * z + x * y]


t = np.linspace(0, 10, 1000)
init_cond = [1, 1, 1]
[x, y, z] = odeint(lorenc, init_cond, t, full_output=False).T
plt.plot(x, z, color='black', linestyle=' ', marker='.',
         markersize=2)
plt.xlabel('x')
plt.ylabel('z')
plt.grid(True)
plt.title("Проекция траектории Лоренца на плоскость xz")
plt.show()
