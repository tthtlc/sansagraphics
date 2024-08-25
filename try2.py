
from sympy import symbols, cos, sin, expand, diff
from sympy.plotting import plot3d_parametric_surface

u, v = symbols('u v')
n = 6  # You can increase this value to see more flipping
x = u - u**(2*n+1)/(2*n+1) + u*v**2
y = -v + v**(2*n+1)/(2*n+1) + v*u**2
z = u**2 - v**2

plot3d_parametric_surface(x, y, z, (u, -1.5, 1.5), (v, -1.5, 1.5))

