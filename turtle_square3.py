
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Square with Turtle Graphics")
screen.bgcolor("white")

# Create a turtle object
square_turtle = turtle.Turtle()
square_turtle.color("black")
square_turtle.pensize(2)  # Set the pen size

# Define the side length of the square
side_length = 100

# Function to draw a square
def draw_square(t, length):
    for _ in range(4):
        t.forward(length)  # Move forward by the specified length
        t.right(90)        # Turn right by 90 degrees

# Position the turtle
square_turtle.penup()
square_turtle.goto(-side_length / 2, side_length / 2)  # Move to the starting position
square_turtle.pendown()

# Draw the square
for theta in range(36):
    square_turtle.forward(side_length*0.1)        # Turn right by 90 degrees
    square_turtle.right(10)        # Turn right by 90 degrees
    draw_square(square_turtle, side_length)

#draw_square(square_turtle, side_length)

# Hide the turtle after drawing
square_turtle.hideturtle()

# Keep the window open until it is closed by the user
screen.mainloop()

