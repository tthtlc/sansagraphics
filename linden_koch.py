#!python3
### https://sites.google.com/site/algorithms2013/home/python-turtle-graphics
# space filling hilbert curve in python 3
# adapted from http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html
import sys, math, time
import turtle as t

## a=> b-a-b
## b=> a+b+a

def a(t, n, angle, length):
    if (n>1):
	a(t, n-1, angle, length)
	t.left(angle)
	a(t, n-1, angle, length)
	t.right(angle)
	t.right(angle)
	a(t, n-1, angle, length)
	t.left(angle)
	a(t, n-1, angle, length)
    else:
	t.forward(length)

## b==> +af-bfb-fa+

def moveto(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

p = t.Pen()
p.reset()
p.down()
p.speed(22)
ts = t.getscreen()
ts.colormode(255)

newlength=100

a(p, 2, 60, newlength)
newlength=newlength/3
moveto(p, 0, 0)

raw_input()
a(p, 3, 60, newlength)
newlength=newlength/3
moveto(p, 0, 0)

raw_input()
a(p, 4, 60, newlength)
newlength=newlength/3
moveto(p, 0, 0)

raw_input()
a(p, 5, 60, newlength)
newlength=newlength/3
moveto(p, 0, 0)

raw_input()
a(p, 6, 60, newlength)
newlength=newlength/3
moveto(p, 0, 0)

