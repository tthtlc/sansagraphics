#!python3
### https://sites.google.com/site/algorithms2013/home/python-turtle-graphics
# space filling hilbert curve in python 3
# adapted from http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html
import sys, math, time
import turtle

count = 0

def moveto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def hilbert(x0, y0, xi, xk, yi, yk, n):
    if n <= 0:
        X = x0 + (xi + yi)/2
        Y = y0 + (xk + yk)/2
        X2 = X * 600 -300
        Y2 = Y * 600 -300
	#print count, X, Y, X2, Y2
	#raw_input()
        global count
        if count < 1:
          count = count + 1
          moveto(X2,Y2)
        turtle.color(X,Y,X*Y)
        turtle.goto(X2,Y2)
    else:
        hilbert(x0,               y0,               yi/2, yk/2, xi/2, xk/2, n - 1)
        hilbert(x0 + xi/2,        y0 + xk/2,        xi/2, xk/2, yi/2, yk/2, n - 1)
        hilbert(x0 + xi/2 + yi/2, y0 + xk/2 + yk/2, xi/2, xk/2, yi/2, yk/2, n - 1)
        hilbert(x0 + xi/2 + yi,   y0 + xk/2 + yk,  -yi/2,-yk/2,-xi/2,-xk/2, n - 1)

        
def main():
    turtle.colormode(1.)
    turtle.speed(0)
    for depth in range(9):
      if 7 > depth > 4:     # for faster rendering.
        turtle.getscreen().tracer(0)
      global count
      count = 0
      hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, depth)
      turtle.getscreen().tracer(1)
      #time.sleep(2)
    turtle.Screen().exitonclick()
  
   
if __name__ == "__main__":
    main()                            
