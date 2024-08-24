
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
u_min, u_max = -5, 5
v_min, v_max = 0, 2 * np.pi
c = 1  # Controls the pitch of the helicoid

# Generate the grid for u and v
u = np.linspace(u_min, u_max, 100)
v = np.linspace(v_min, v_max, 100)
u, v = np.meshgrid(u, v)

# Parametric equations of the helicoid
x = u * np.cos(v)
y = u * np.sin(v)
z = c * v

# Plotting the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Helicoid Surface')

plt.show()

