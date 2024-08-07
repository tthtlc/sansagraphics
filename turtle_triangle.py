
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Square with Turtle Graphics")
screen.bgcolor("white")

# Create a turtle object
triangle_turtle = turtle.Turtle()
triangle_turtle.color("black")
triangle_turtle.pensize(2)  # Set the pen size

# Define the side length of the triangle
side_length = 100

# Function to draw a triangle
def draw_triangle(t, length):
    for _ in range(3):
        t.forward(length)  # Move forward by the specified length
        t.right(120)        # Turn right by 90 degrees

# Position the turtle
triangle_turtle.penup()
triangle_turtle.goto(-side_length / 2, side_length / 2)  # Move to the starting position
triangle_turtle.pendown()
triangle_turtle.right(10)        # Turn right by 90 degrees
draw_triangle(triangle_turtle, side_length)
triangle_turtle.right(10)        # Turn right by 90 degrees
draw_triangle(triangle_turtle, side_length)

# Draw the triangle
for theta in range(36):
    triangle_turtle.right(10)        # Turn right by 90 degrees
    draw_triangle(triangle_turtle, side_length)

#draw_triangle(triangle_turtle, side_length)

# Hide the turtle after drawing
triangle_turtle.hideturtle()

# Keep the window open until it is closed by the user
screen.mainloop()

