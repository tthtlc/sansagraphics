

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the cardioid parametric equations
def cardioid(t, a=1):
    x = a * (1 + np.cos(t)) * np.cos(t)
    y = a * (1 + np.cos(t)) * np.sin(t)
    return x, y

# Define the tangent vector at each point on the cardioid
def tangent_vector(t, a=1):
    x_prime = a * (-np.sin(t) - 2 * np.sin(t) * np.cos(t))
    y_prime = a * (2 * np.cos(t) - 1)
    return x_prime, y_prime

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid(True)

# Create line objects for the cardioid and the tangent vector
line, = ax.plot([], [], 'r-', lw=2, label='Cardioid')
tangent_line, = ax.plot([], [], 'b-', lw=1, label='Tangent Vector')

# Initialize the animation
def init():
    line.set_data([], [])
    tangent_line.set_data([], [])
    return line, tangent_line

# Animation function
def animate(t):
    # Calculate cardioid point
    x, y = cardioid(t)

    # Calculate tangent vector
    x_prime, y_prime = tangent_vector(t)

    # Normalize the tangent vector
    norm = np.sqrt(x_prime**2 + y_prime**2)
    x_prime /= norm
    y_prime /= norm

    # Set the cardioid line data
    line.set_data([0, x], [0, y])

    # Set the tangent vector line data
    tangent_line.set_data([x, x + x_prime], [y, y + y_prime])

    return line, tangent_line

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=np.linspace(0, 2*np.pi, 200),
    interval=50, blit=True
)

# Display the plot
plt.legend()
plt.title('Cardioid and Tangent Vector')
plt.show()

