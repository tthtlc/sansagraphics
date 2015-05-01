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
	b(t, n-1, angle, length)
	t.left(angle)
	a(t, n-1, angle, length)
	t.left(angle)
	b(t, n-1, angle, length)
    else:
	t.forward(length)

## b==> +af-bfb-fa+

def b(t, n, angle, length):
    if (n>1):
	a(t, n-1, angle, length)
	t.right(angle)
	b(t, n-1, angle, length)
	t.right(angle)
	a(t, n-1, angle, length)
    else:
	t.forward(length)

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
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)
t.right(60)

raw_input()
a(p, 3, 60, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)
t.right(60)

raw_input()
a(p, 4, 60, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)
t.right(60)

raw_input()
a(p, 5, 60, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)
t.right(60)

raw_input()
a(p, 6, 60, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)
t.right(60)

raw_input()
a(p, 8, 60, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)
t.right(60)

raw_input()
a(p, 10, 60, newlength)
newlength=newlength/2
moveto(p, -newlength+newlength/2, -newlength+newlength/2)
t.right(60)
