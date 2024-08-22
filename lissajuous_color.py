
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

# Parameters
#a, b, c, d, e, f = 3, 2, 4, 1, 5, 3
a, b, c, d, e, f = 3, 2, 3, 2, 3, 3
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

# Parametric Equations
x = np.sin(a * u) * np.cos(b * v)
y = np.sin(c * u) * np.sin(d * v)
z = np.cos(e * u + f * v)

# Color map
colors = cm.viridis(np.linspace(0, 1, x.shape[0]))

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each segment with a different color
for i in range(x.shape[0]):
    ax.plot(x[i, :], y[i, :], z[i, :], color=colors[i])

ax.set_box_aspect([1, 1, 1])  # Aspect ratio is 1:1:1
plt.show()

