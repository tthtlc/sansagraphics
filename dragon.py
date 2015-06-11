import sys
import turtle as t

p = t.Pen()
p.reset()
p.down()
p.speed(100)
pencolour=["green","cyan","blue","violet", "red", "yellow"]
t.pencolor(pencolour[2])

def dragon(t, length, level):
	if level>0:
		t.left(90)
		t.forward(length/2)
		dragon(t, length/2, level-1)
		t.forward(length/2)
		t.right(90)
		t.forward(length/2)
		dragon(t, length/2, level-1)
		t.forward(length/2)
		t.right(90)
		t.forward(length/2)
		dragon(t, length/2, level-1)
		t.forward(length/2)
		t.left(90)
	
dragon(t, 100, 5)
raw_input()
sys.exit(0)


