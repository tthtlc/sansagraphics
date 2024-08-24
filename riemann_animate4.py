


import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import random

# Define the parameters for the surface
u, v = sp.symbols('u v')
a = 1  # Constant parameter to change the shape of the surface

# Function to update the surface for different m and n values
def update_surface(m, n, k):
    # Define the parametric equations for the Riemann surface
    #x_expr = a * sp.cosh(v) * sp.cos(u)
    #y_expr = a * sp.cosh(v) * sp.sin(u) 
    #z_expr = a * sp.sinh(v)

    # New parametric equations
    x_expr = a * sp.cosh(m * v) * sp.cos(u) * sp.cos(k * v)
    y_expr = a * sp.cosh(n * v) * sp.sin(u) * sp.cos(k * v)
    z_expr = a * sp.sinh(v)

    # Convert SymPy expressions to numerical functions
    x_func = sp.lambdify((u, v), x_expr, "numpy")
    y_func = sp.lambdify((u, v), y_expr, "numpy")
    z_func = sp.lambdify((u, v), z_expr, "numpy")

    # Generate a grid for u and v
    u_vals = np.linspace(0, 4 * np.pi, 100)
    v_vals = np.linspace(-2, 2, 50)
    u_grid, v_grid = np.meshgrid(u_vals, v_vals)

    # Compute the x, y, z coordinates of the surface
    x_vals = x_func(u_grid, v_grid)
    y_vals = y_func(u_grid, v_grid)
    z_vals = z_func(u_grid, v_grid)

    return x_vals, y_vals, z_vals

# Set up the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Animation update function
def animate(i):
    ax.clear()
    m = random.uniform(0.5, 10.0)  # Generate random m between 0.5 and 2.0
    n = random.uniform(0.5, 10.0)  # Generate random n between 0.5 and 2.0
    k = random.uniform(0.5, 20.0)  # Generate random n between 0.5 and 2.0
    x_vals, y_vals, z_vals = update_surface(m, n, k)
    ax.plot_surface(x_vals, y_vals, z_vals, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(f'Riemann Surface (m={m:.2f}, n={n:.2f})')

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=1000)

# Display the animation
plt.show()

