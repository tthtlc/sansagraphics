
import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a = 5  # Semi-major axis length
b = 3  # Semi-minor axis length

# Calculate the distance from the center to each focus
c = np.sqrt(a**2 - b**2)

# Define the foci
focus1 = (-c, 0)
focus2 = (c, 0)

# Generate theta values from 0 to 2π for a full ellipse
theta = np.linspace(0, 2 * np.pi, 1000)

# Parametric equations for the ellipse
x = a * np.cos(theta)
y = b * np.sin(theta)

# Plot the ellipse
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Ellipse')

# Plot the foci
plt.scatter(*focus1, color='red', zorder=5, label='Focus 1')
plt.scatter(*focus2, color='blue', zorder=5, label='Focus 2')

# Draw lines from the foci to a point on the ellipse
# Here, we choose the point corresponding to theta = π/4 for demonstration
point_idx = 125  # Corresponds to θ = π/4
ellipse_point = (x[point_idx], y[point_idx])

plt.plot([focus1[0], ellipse_point[0]], [focus1[1], ellipse_point[1]], 'r--', label='Line to Ellipse Point')
plt.plot([focus2[0], ellipse_point[0]], [focus2[1], ellipse_point[1]], 'b--', label='Line to Ellipse Point')

# Plot the selected point on the ellipse
plt.scatter(*ellipse_point, color='green', zorder=5, label='Point on Ellipse')

# Add labels and legend
plt.title('Elliptical Line from Foci')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.axis('equal')
plt.show()

