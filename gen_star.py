
import turtle
import math as math
import numpy as np

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Star with Turtle Graphics")
screen.bgcolor("white")

# Create a turtle object
star_turtle = turtle.Turtle()
star_turtle.color("black")
star_turtle.pensize(2)  # Set the pen size

# Define the side length of the star
side_length = 50
radius = 4*side_length
total_range = 18
angle_quantum=2*math.pi/total_range

# Function to draw a star
def draw_star(t, length, ngon):
    star_angle=(360*4/ngon)
    for _ in range(ngon):
        t.forward(length)  # Move forward by the specified length
        t.right(star_angle)        # Turn right by 90 degrees

# Position the turtle

# Draw the star
angle=0
for ngon in range(3,total_range):
    #star_turtle.forward(side_length*0.1)        # Turn right by 90 degrees
    star_turtle.penup()
    xcoord = radius * np.cos( angle)
    ycoord = radius * np.sin( angle)
    angle += angle_quantum
    star_turtle.goto(xcoord, ycoord)  # Move to the starting position
    star_turtle.pendown()
    draw_star(star_turtle, side_length, ngon)

#draw_star(star_turtle, side_length)

# Hide the turtle after drawing
star_turtle.hideturtle()

# Keep the window open until it is closed by the user
screen.mainloop()

