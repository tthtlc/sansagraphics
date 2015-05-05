
import turtle as t
p = t.Pen()
p.reset()
p.down()
p.speed(22)
ts = t.getscreen()
ts.colormode(255)

##https://vrmath2.net/content/recursive-2d-fern-leaf-procedure

def fern(t, size, sign):
    """
       Make turtle t draw a Koch fractal of 'size' and 'sign'.
       Leave the turtle facing the same direction.
    """

    if size > 1:          # The base case is just a straight line
        t.forward(size)
        t.right(70*sign)
        fern(t, size * 0.5, sign*-1)   # Go 1/3 of the way
        t.left(70*sign)
        t.forward(size)
        t.left(70*sign)
        fern(t, size * 0.5, sign)
        t.right(70*sign)
        t.right(7*sign)
        fern(t, size -1 , sign)
        t.left(7*sign)
        #t.left(60)
        #fern(t, size-1, sign/3)


fern(t, 16, 1)
