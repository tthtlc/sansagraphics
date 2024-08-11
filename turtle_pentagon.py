
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Star with Turtle Graphics")
screen.bgcolor("white")

# Create a turtle object
star_turtle = turtle.Turtle()
star_turtle.color("black")
star_turtle.pensize(2)  # Set the pen size

# Define the side length of the star
side_length = 100
star_angle=(4*360/5)

# Function to draw a star
def draw_star(t, length):
    for _ in range(5):
        t.forward(length)  # Move forward by the specified length
        t.right(star_angle)        # Turn right by 90 degrees

# Position the turtle
star_turtle.penup()
star_turtle.goto(-side_length / 2, side_length / 2)  # Move to the starting position
star_turtle.pendown()

# Draw the star
for theta in range(36):
    #star_turtle.forward(side_length*0.1)        # Turn right by 90 degrees
    star_turtle.right(10)        # Turn right by 90 degrees
    draw_star(star_turtle, side_length)

#draw_star(star_turtle, side_length)

# Hide the turtle after drawing
star_turtle.hideturtle()

# Keep the window open until it is closed by the user
screen.mainloop()

