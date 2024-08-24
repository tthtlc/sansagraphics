
import numpy as np
import matplotlib.pyplot as plt

def leaf_shape(t):
    """Generates the x and y coordinates for a leaf shape."""
    x = np.sin(t) * np.cos(t)
    y = np.sin(t)**2
    return x, y

def draw_leaf(ax, scale=1.0, rotation=0.0, color='green'):
    """Draws a leaf on the given axis."""
    t = np.linspace(0, 2 * np.pi, 100)
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
    
    # Draw multiple leaves with different scales and rotations
    draw_leaf(ax, scale=1.0, rotation=0.0)
    draw_leaf(ax, scale=0.8, rotation=np.pi/4, color='darkgreen')
    draw_leaf(ax, scale=0.6, rotation=np.pi/2, color='lightgreen')
    
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')  # Turn off the axis
    
    plt.show()

if __name__ == "__main__":
    main()

