
import numpy as np
import matplotlib.pyplot as plt

def leaf_shape(t):
    """Generates the x and y coordinates for a leaf shape with a sharper tip."""
    x = np.sin(t) * np.cos(t)
    y = np.sin(t) * np.abs(np.cos(t))
    return x, y

def draw_leaf(ax, scale=1.0, rotation=0.0, color='green'):
    """Draws a leaf on the given axis."""
    t = np.linspace(-np.pi / 2, np.pi / 2, 1000)
    x, y = leaf_shape(t)
    
    # Apply scaling
    x *= scale
    y *= scale
    
    # Apply rotation
    x_rot = x * np.cos(rotation) - y * np.sin(rotation)
    y_rot = x * np.sin(rotation) + y * np.cos(rotation)
    
    ax.plot(x_rot, y_rot, color=color)

def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    
    # Draw a single leaf with a sharp tip
    draw_leaf(ax, scale=1.0, rotation=10.0, color='green')
    
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1, 1)
    ax.axis('off')  # Turn off the axis
    
    plt.show()

if __name__ == "__main__":
    main()

