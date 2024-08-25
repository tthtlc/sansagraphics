
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

# Constants for the torus
R = 2  # Major radius
r = 0.5  # Minor radius

# Parametric equations for a torus
x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)

# Adding gyroidal deformation
gx = np.sin(u) * np.cos(v)
gy = np.sin(v) * np.cos(u)
gz = np.sin(u + v)

# Gyroidal Torus surface
x = x + 0.3 * gx
y = y + 0.3 * gy
z = z + 0.3 * gz

# Plotting the surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Setting the title and labels
ax.set_title('Gyroidal Torus Surface')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

