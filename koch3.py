
import turtle as t
t.hideturtle()
t.penup()
t.setx(-300)
t.sety(-300)
p = t.Pen()
p.reset()
p.speed(22)
t.showturtle()
t.pendown()

def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

koch(t, 4, 1000)
raw_input()
