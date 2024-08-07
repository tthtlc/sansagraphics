
import matplotlib.pyplot as plt
import numpy as np

def plot_chasing_diagram():
    # Define the triangle vertices
    A = np.array([0, 0])
    B = np.array([4, 0])
    C = np.array([0, 3])

    # Define the points for squares
    D = B + (C - A)
    E = C + (B - A)

    # Calculate additional points for constructing squares
    F = C + (B - A)
    G = A + (C - A)
    H = B + (D - B)
    I = C + (D - C)
    J = A + (B - A)

    # Plot triangle
    plt.plot([A[0], B[0]], [A[1], B[1]], 'k-')
    plt.plot([B[0], C[0]], [B[1], C[1]], 'k-')
    plt.plot([C[0], A[0]], [C[1], A[1]], 'k-')

    # Plot squares
    plt.plot([A[0], C[0]], [A[1], C[1]], 'b-')
    plt.plot([C[0], E[0]], [C[1], E[1]], 'b-')
    plt.plot([E[0], D[0]], [E[1], D[1]], 'b-')
    plt.plot([D[0], B[0]], [D[1], B[1]], 'b-')

    plt.plot([A[0], G[0]], [A[1], G[1]], 'r-')
    plt.plot([G[0], F[0]], [G[1], F[1]], 'r-')
    plt.plot([F[0], C[0]], [F[1], C[1]], 'r-')

    plt.plot([B[0], J[0]], [B[1], J[1]], 'g-')
    plt.plot([J[0], I[0]], [J[1], I[1]], 'g-')
    plt.plot([I[0], C[0]], [I[1], C[1]], 'g-')

    # Label the points
    plt.text(A[0], A[1], 'A', fontsize=12, ha='right', va='top')
    plt.text(B[0], B[1], 'B', fontsize=12, ha='left', va='top')
    plt.text(C[0], C[1], 'C', fontsize=12, ha='right', va='bottom')
    plt.text(D[0], D[1], 'D', fontsize=12, ha='left', va='bottom')
    plt.text(E[0], E[1], 'E', fontsize=12, ha='right', va='bottom')
    plt.text(F[0], F[1], 'F', fontsize=12, ha='right', va='top')
    plt.text(G[0], G[1], 'G', fontsize=12, ha='right', va='bottom')
    plt.text(H[0], H[1], 'H', fontsize=12, ha='left', va='bottom')
    plt.text(I[0], I[1], 'I', fontsize=12, ha='right', va='top')
    plt.text(J[0], J[1], 'J', fontsize=12, ha='left', va='bottom')

    # Set plot limits and show grid
    plt.xlim(-1, 7)
    plt.ylim(-1, 5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    # Show plot
    plt.title("Euclid's Proof of the Pythagorean Theorem")
    plt.show()

plot_chasing_diagram()

