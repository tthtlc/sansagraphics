#!python3
### https://sites.google.com/site/algorithms2013/home/python-turtle-graphics
# space filling hilbert curve in python 3
# adapted from http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html
import sys, math, time
import turtle as t

## a=> -bf+afa+fb-

def a(t, n, angle, length):
    if (n>1):
	t.left(angle)
	b(t, n-1, angle, length)
	t.forward(length)
	t.right(angle)
	a(t, n-1, angle, length)
	t.forward(length)
	a(t, n-1, angle, length)
	t.right(angle)
	t.forward(length)
	b(t, n-1, angle, length)
	t.left(angle)

## b==> +af-bfb-fa+

def b(t, n, angle, length):
    if (n>1):
	t.right(angle)
	a(t, n-1, angle, length)
	t.forward(length)
	t.left(angle)
	b(t, n-1, angle, length)
	t.forward(length)
	b(t, n-1, angle, length)
	t.left(angle)
	t.forward(length)
	a(t, n-1, angle, length)
	t.right(angle)

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
angle=90

newlength=300

a(p, 2, 90, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)

a(p, 3, 90, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)

raw_input()
a(p, 4, 90, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)

raw_input()
a(p, 5, 90, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)

raw_input()
a(p, 6, 90, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)

