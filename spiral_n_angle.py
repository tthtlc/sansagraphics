import math
 
n = 3
 
import turtle as t

def draw_n_angle(nos_angle, max_turns):
	p = t.Pen()
	p.reset()
	p.down()
	p.speed(0)
	l=0
	j=0
	k=0
	ts = t.getscreen()
        ts.clear()
	ts.colormode(255)
	angle=360/nos_angle
	for i in range(max_turns): 
		p.forward(i*3)
		p.left(angle)
		p.left(1)
	###	p.pencolor((0.2,0.8,0.55))
		j = (j+2)%256
		k = (k+2)%256
		l = (l+2)%256
		p.pencolor((j,k,l))

while True:
 
    draw_n_angle(n,60)
    n = n+1
 
    print "Press enter.."
    raw = raw_input()
 
a = raw_input()
