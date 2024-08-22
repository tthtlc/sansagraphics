
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

a, b, c, d, e, f = 3, 2, 4, 1, 5, 3

x = np.sin(a * u) * np.cos(b * v)
y = np.sin(c * u) * np.sin(d * v)
z = np.cos(e * u + f * v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z, color='black')
plt.show()

