
import numpy as np
import matplotlib.pyplot as plt

def draw_concentric_circles(ax, center, max_radius, num_circles):
    for i in range(1, num_circles + 1):
        radius = max_radius * i / num_circles
        circle = plt.Circle(center, radius, color='black', fill=False, linewidth=1.5)
        ax.add_artist(circle)

def main():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')

    # Parameters
    num_circles = 15  # Number of concentric circles in each pattern
    radius = 1        # Radius of the largest circle
    spacing = radius * 2
    grid_size = 3     # 3x3 grid

    # Generate the grid of concentric circles
    for i in range(grid_size):
        for j in range(grid_size):
            x_offset = i * spacing
            y_offset = j * spacing
            center = (x_offset, y_offset)
            draw_concentric_circles(ax, center, radius, num_circles)

    plt.xlim(-radius, grid_size * spacing - radius)
    plt.ylim(-radius, grid_size * spacing - radius)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()

