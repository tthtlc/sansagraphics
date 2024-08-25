
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create the figure and the 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Initialize parameters
u = np.linspace(-1.5, 1.5, 100)
v = np.linspace(-1.5, 1.5, 100)
u, v = np.meshgrid(u, v)

# Function to update the plot for each frame
def update(order):
    ax.clear()
    x = u
    y = v
    z = u**2 - v**2
    for n in range(2, order + 1, 2):  # Increment in even steps
        x = x + (u**n) / n - (u*v**2) / n
        y = y + (v**n) / n - (v*u**2) / n

    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title(f'Enneper Surface of Order {order}')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_zlim(-2, 2)

# Generate animation
ani = FuncAnimation(fig, update, frames=range(2, 11, 2), repeat=True)

# Save animation as gif
ani.save('enneper_surface_even_order_animation.gif', writer='imagemagick', fps=1)

plt.show()

