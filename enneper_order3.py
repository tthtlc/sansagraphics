
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of parameters u and v
u = np.linspace(-2, 2, 100)
v = np.linspace(-2, 2, 100)
u, v = np.meshgrid(u, v)

# Define the Enneper surface of order 3
x = u - (u**5)/5 + u*(v**2) - (u**3)*(v**2)/3
y = v - (v**5)/5 + v*(u**2) - (v**3)*(u**2)/3
z = u**2 - v**2

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels and title
ax.set_title('Enneper Surface of Order 3')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

