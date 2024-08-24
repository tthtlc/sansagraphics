

import numpy as np
import matplotlib.pyplot as plt

def draw_circle(ax, center, radius, color='black', linewidth=1):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    ax.plot(x, y, color=color, linewidth=linewidth)

def draw_ellipses(ax, centers, major_radius, minor_radius, angle_offset=0):
    for center in centers:
        theta = np.linspace(0, 2 * np.pi, 100)
        x = center[0] + major_radius * np.cos(theta + angle_offset)
        y = center[1] + minor_radius * np.sin(theta)
        ax.plot(x, y, color='black', linewidth=1)

def draw_spherical_grid(ax, radius, num_lines):
    for i in range(1, num_lines):
        theta = np.linspace(0, 2 * np.pi, 500)
        r = radius * (i / num_lines)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        ax.plot(x, y, color='black', linewidth=0.5)

        phi = np.linspace(0, np.pi, num_lines)
        for p in phi:
            x = radius * np.sin(p) * np.cos(theta)
            y = radius * np.sin(p) * np.sin(theta)
            ax.plot(x, y, color='black', linewidth=0.5)

def draw_symmetric_pattern(ax, center, radius, num_points, num_petals):
    angles = np.linspace(0, 2 * np.pi, num_petals, endpoint=False)
    for angle in angles:
        for i in range(1, num_points):
            t = np.linspace(0, np.pi, 100)
            x = center[0] + radius * np.cos(t) * np.cos(angle)
            y = center[1] + radius * np.sin(t) * np.sin(angle)
            ax.plot(x, y, color='black', linewidth=1)

def main():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw spherical grid
    draw_spherical_grid(ax, radius=3, num_lines=10)
    
    # Draw central circles
    draw_circle(ax, center=(0, 0), radius=1.5)
    draw_circle(ax, center=(0, 0), radius=3)
    
    # Draw ellipses forming the petal-like structure
    centers = [(0, 0), (0, 1.5), (1.5, 0), (-1.5, 0), (0, -1.5)]
    draw_ellipses(ax, centers, major_radius=1.5, minor_radius=0.75)
    
    # Draw symmetric pattern
    draw_symmetric_pattern(ax, center=(0, 0), radius=1.5, num_points=5, num_petals=8)

    plt.show()

if __name__ == "__main__":
    main()

