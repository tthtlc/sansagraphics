
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def enneper_surface(u, v, n):
    x = u - u**(2*n+1)/(2*n+1) + u*v**2
    y = -v + v**(2*n+1)/(2*n+1) + v*u**2
    z = u**2 - v**2
    return x, y, z

u = np.linspace(-2, 2, 50)
v = np.linspace(-2, 2, 50)
U, V = np.meshgrid(u, v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n_values = range(1, 5)

for n in n_values:
    X, Y, Z = enneper_surface(U, V, n)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='c', alpha=0.6, edgecolor='none')
    plt.pause(1)  # Pause to show the current surface

plt.show()

