
import numpy as np
import matplotlib.pyplot as plt

def draw_sphere_grid(ax, num_lines=20):
    u = np.linspace(0, 2 * np.pi, num_lines)
    v = np.linspace(0, np.pi, num_lines)
    
    for i in u:
        ax.plot(np.sin(i)*np.outer(np.ones(np.size(v)), np.sin(v)),
                np.cos(i)*np.outer(np.ones(np.size(v)), np.sin(v)),
                np.outer(np.ones(np.size(v)), np.cos(v)),
                color='black', linewidth=0.5)

    for j in v:
        ax.plot(np.sin(u)*np.outer(np.sin(j), np.ones(np.size(u))),
                np.cos(u)*np.outer(np.sin(j), np.ones(np.size(u))),
                np.outer(np.cos(j), np.ones(np.size(u))),
                color='black', linewidth=0.5)

def draw_flower_pattern(ax, num_petals=4):
    angles = np.linspace(0, 2 * np.pi, num_petals, endpoint=False)
    radius = 1
    for angle in angles:
        theta = np.linspace(0, 2 * np.pi, 100)
        x = radius * np.cos(theta) * np.cos(angle) - radius * np.sin(theta) * np.sin(angle)
        y = radius * np.cos(theta) * np.sin(angle) + radius * np.sin(theta) * np.cos(angle)
        ax.plot(x, y, color='black', linewidth=1)

def main():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw the sphere grid pattern
    draw_sphere_grid(ax)
    
    # Draw the flower pattern
    draw_flower_pattern(ax, num_petals=8)

    plt.show()

if __name__ == "__main__":
    main()

