
import numpy as np
import sympy as sp
from sympy.plotting import plot3d_parametric_surface

# Define the parameters for the surface
u, v = sp.symbols('u v')
a = 1 # You can adjust this parameter to change the shape of the surface


# Define the parametric equations for the Riemann surface
x = (a * sp.cosh(2*v) * sp.cos(u))
y = (a * sp.cosh(v) * sp.sin(2*u))
z = (a * sp.sinh(v))

# Plot the surface
plot3d_parametric_surface(
    (x, y, z),
    (u, 0, 4 * sp.pi),
    (v, -2, 2),  # Adjust v range to extend or shorten the surface along z-axis
    xlabel='x',
    ylabel='y',
    zlabel='z',
    title='Riemann Surface'
)

