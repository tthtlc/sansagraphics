
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define the range of parameters u and v
u = np.linspace(-2, 2, 100)
v = np.linspace(-2, 2, 100)
u, v = np.meshgrid(u, v)

# Function to generate the Enneper surface for a given order n
def enneper_surface(u, v, n):
    x = u - (u**(2*n-1))/(2*n-1) + u*v**2
    y = v - (v**(2*n-1))/(2*n-1) + v*u**2
    z = u**2 - v**2
    return x, y, z

# Create the figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot for each frame
def update(n):
    ax.clear()
    x, y, z = enneper_surface(u, v, n)
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title(f'Enneper Surface of Order {n}')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_zlim(-2, 2)

# Generate animation
ani = FuncAnimation(fig, update, frames=range(2, 10), repeat=True)

# Save the animation as a gif (optional)
# ani.save('enneper_surface_animation.gif', writer='imagemagick', fps=1)

plt.show()

