
import turtle
import numpy as np

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Star with Turtle Graphics")
screen.bgcolor("white")

# Create a turtle object
cardiod_turtle = turtle.Turtle()
cardiod_turtle.color("black")
cardiod_turtle.pensize(2)  # Set the pen size

# Define the side length of the cardiod
side_length = 100
cardiod_angle=(720/5)

import math as math
# Function to draw a cardiod
def draw_cardiod(t, length):
    for param in range(20):
        x,y=cardioid(param, a=1)
        t.forward(x)  # Move forward by the specified length
        t.right(y)        # Turn right by 90 degrees

# Define the cardioid parametric equations
def cardioid(t, a=1):
    x = a * (1 + np.cos(t)) * np.cos(t)
    y = a * (1 + np.cos(t)) * np.sin(t)
    return x, y

# Position the turtle
cardiod_turtle.penup()
cardiod_turtle.goto(-side_length / 2, side_length / 2)  # Move to the cardiodting position
cardiod_turtle.pendown()

# Draw the cardiod
for theta in range(300):
    #cardiod_turtle.forward(side_length*0.1)        # Turn right by 90 degrees
    #cardiod_turtle.right(10)        # Turn right by 90 degrees
    draw_cardiod(cardiod_turtle, theta)

#draw_cardiod(cardiod_turtle, side_length)

# Hide the turtle after drawing
cardiod_turtle.hideturtle()

# Keep the window open until it is closed by the user
screen.mainloop()

