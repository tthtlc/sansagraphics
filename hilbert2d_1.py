
import turtle
from turtle import left, right, forward


def hilbert(level, angle):
    if level == 0:
        return

    size = 300 / level 
    turtle.color("Blue")
    turtle.speed("Fastest")

    right(angle)
    hilbert(level - 1, -angle)
    forward(size)
    left(angle)
    hilbert(level - 1, angle)
    forward(size)
    hilbert(level - 1, angle)
    left(angle)
    forward(size)
    hilbert(level - 1, -angle)
    right(angle)

hilbert(3, 90)
raw_input()
