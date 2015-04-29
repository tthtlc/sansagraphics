
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
    if order == 0:
        t.forward(size)
    else:
        for angle in [80, -160, 80, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

#p.up()
koch(t, 4, 500)
a = raw_input()

