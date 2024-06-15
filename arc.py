
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def draw_arc(radius, start_angle, end_angle, num_segments):
    glBegin(GL_LINE_STRIP)
    for i in range(num_segments + 1):
        theta = start_angle + (end_angle - start_angle) * i / num_segments
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        glVertex2f(x, y)
    glEnd()

def main():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 800, "Dome Arc", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the viewport
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-15, 15, -15, 15, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    radius = 10
    start_angle = 0
    end_angle = np.pi/3
    num_segments = 100

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the arc
        glColor3f(1.0, 1.0, 1.0)
        draw_arc(radius, start_angle, end_angle, num_segments)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()

