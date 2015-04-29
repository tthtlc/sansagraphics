
import turtle as t
t.hideturtle()
t.penup()
#t.setx(-300)
#t.sety(-300)
p = t.Pen()
p.reset()
p.speed(22)
t.showturtle()
t.pendown()

def koch(t, order, size, myangle):
    if order == 0:
        t.forward(size)
        t.left(myangle)
    else:
        for angle in [60, -60, -60, 60, 0]:
           koch(t, order-1, size/3, angle/2)
           t.left(angle)

#p.up()
koch(t, 3, 500, 60)
a = raw_input()

