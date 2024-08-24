
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def costa_surface(u, v, a=1, b=1):
    """Generate Costa surface coordinates."""
    x = np.cosh(u) * np.sin(v) * np.sqrt(a)
    y = np.sinh(u) * np.cos(v) * np.sqrt(b)
    z = -np.log(np.tanh(u / 2))
    return x, y, z

# Create a meshgrid
u = np.linspace(-2, 2, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

# Generate Costa surface
x, y, z = costa_surface(u, v)

# Plotting the surface
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b', edgecolor='k', alpha=0.8)

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Costa Surface (Genus 1, 3 Ends)")

plt.show()

