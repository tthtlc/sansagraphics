
import numpy as np
import matplotlib.pyplot as plt

def draw_grid(ax, radius, num_lines):
    # Draw grid lines resembling latitude and longitude on a sphere
    for i in range(num_lines):
        theta = np.linspace(0, 2 * np.pi, 500)
        r = radius * (i + 1) / num_lines
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        ax.plot(x, y, color='black', linewidth=0.5)
        
        for angle in np.linspace(0, np.pi, num_lines):
            x = r * np.cos(angle)
            y = np.linspace(-r, r, 500)
            ax.plot(x * np.ones_like(y), y, color='black', linewidth=0.5)

def draw_ellipses(ax, num_ellipses, radius):
    angles = np.linspace(0, np.pi / 2, num_ellipses)
    for angle in angles:
        t = np.linspace(0, 2 * np.pi, 500)
        x = radius * np.cos(t) * np.cos(angle)
        y = radius * np.sin(t)
        ax.plot(x, y, color='black', linewidth=1)
        ax.plot(-x, y, color='black', linewidth=1)
        ax.plot(x, -y, color='black', linewidth=1)
        ax.plot(-x, -y, color='black', linewidth=1)

def draw_symmetry(ax, radius, num_lines):
    angles = np.linspace(0, 2 * np.pi, num_lines, endpoint=False)
    for angle in angles:
        t = np.linspace(0, 2 * np.pi, 500)
        x = radius * np.cos(t) * np.cos(angle)
        y = radius * np.sin(t) * np.sin(angle)
        ax.plot(x, y, color='black', linewidth=1)

def main():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw the spherical grid pattern
    draw_grid(ax, radius=3, num_lines=10)
    
    # Draw the elliptical flower pattern
    draw_ellipses(ax, num_ellipses=4, radius=2)
    
    # Draw the symmetrical pattern
    draw_symmetry(ax, radius=2, num_lines=8)
    
    plt.show()

if __name__ == "__main__":
    main()

