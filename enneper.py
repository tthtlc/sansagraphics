
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the surface
u, v = sp.symbols('u v')
a = 2  # Scale parameter

# Define the parametric equations for the surface
x_expr = u - (u**3)/3 + u*v**2
y_expr = v - (v**3)/3 + v*u**2
z_expr = u**2 - v**2

# Convert SymPy expressions to numerical functions
x_func = sp.lambdify((u, v), x_expr, "numpy")
y_func = sp.lambdify((u, v), y_expr, "numpy")
z_func = sp.lambdify((u, v), z_expr, "numpy")

# Generate a grid for u and v
u_vals = np.linspace(-1.5, 1.5, 100)
v_vals = np.linspace(-1.5, 1.5, 100)
u_grid, v_grid = np.meshgrid(u_vals, v_vals)

# Compute the x, y, z coordinates of the surface
x_vals = x_func(u_grid, v_grid)
y_vals = y_func(u_grid, v_grid)
z_vals = z_func(u_grid, v_grid)

# Set up the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_wireframe(x_vals, y_vals, z_vals, color='purple', linewidth=0.5)

# Customize the plot
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Enneper Surface')

# Adjust the view angle for better visualization
ax.view_init(elev=30, azim=60)

# Show the plot
plt.show()

