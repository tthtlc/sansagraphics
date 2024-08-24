
import numpy as np
import matplotlib.pyplot as plt

def draw_circle(ax, radius, center=(0, 0), num_points=100, **kwargs):
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    ax.plot(x, y, **kwargs)

def draw_flower_pattern(ax, num_petals=4, petal_radius=1, petal_width=0.1, **kwargs):
    angles = np.linspace(0, 2 * np.pi, num_petals, endpoint=False)
    for angle in angles:
        for scale in [1, 1.5, 2]:  # Different scales for layering effect
            x = scale * petal_radius * np.cos(angle)
            y = scale * petal_radius * np.sin(angle)
            draw_circle(ax, petal_radius * scale, center=(x, y), **kwargs)

def draw_grid_pattern(ax, num_lines=10, radius=3, **kwargs):
    for i in range(1, num_lines + 1):
        draw_circle(ax, radius * i / num_lines, **kwargs)

def main():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw the grid pattern on the sphere
    draw_grid_pattern(ax, num_lines=20, radius=3, color='black', linewidth=0.5)
    
    # Draw the central flower pattern with symmetry
    draw_flower_pattern(ax, num_petals=8, petal_radius=0.75, color='black', linewidth=1)

    plt.show()

if __name__ == "__main__":
    main()

