import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation

# Initialize parameters
a, b, c, d, e, f = 3, 2, 4, 1, 5, 3
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

# Set up figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Color map
colors = cm.viridis(np.linspace(0, 1, u.shape[0]))

# Initialize the plot with an empty plot
lines = []
for i in range(u.shape[0]):
    line, = ax.plot([], [], [], color=colors[i])
    lines.append(line)

ax.set_box_aspect([1, 1, 1])

# Update function for animation
def update(frame):
    ax.clear()  # Clear the previous frame
    a = 3 + np.sin(frame / 10)  # Slowly vary parameter 'a'

    # Recalculate the parametric equations
    x = np.sin(a * u) * np.cos(b * v)
    y = np.sin(c * u) * np.sin(d * v)
    z = np.cos(e * u + f * v)

    # Update each segment with the new values
    for i in range(x.shape[0]):
        ax.plot(x[i, :], y[i, :], z[i, :], color=colors[i])

    ax.set_box_aspect([1, 1, 1])
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=100)

plt.show()

