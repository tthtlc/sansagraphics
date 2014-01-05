
import turtle as t
p = t.Pen()
p.reset()
p.down()
p.speed(22)
l=0
j=0
k=0
ts = t.getscreen()
ts.colormode(255)
angle=360/3
for i in range(1000): 
	p.forward(i*3) 
	p.left(angle)
	p.left(1)
###	p.pencolor((0.2,0.8,0.55))
	j = (j+2)%256
	k = (k+2)%256
	l = (l+2)%256
	p.pencolor((j,k,l))
a = raw_input()
