import sys
import turtle as t

p = t.Pen()
p.reset()
p.down()
p.speed(100)
max_level=5
length=300.0/max_level
pencolour=["green","cyan","blue","violet", "red", "yellow"]

def myngon(t, side_number, level):
	global length
	t.pencolor(pencolour[level])
	for i in range(side_number):
		t.forward(length*level)
		angle=360/side_number
		if level>1:
			t.left((180-angle)/2)
			myngon(t, side_number, level-1)
			t.right((180-angle)/2)
		t.left(angle)
	
myngon(t, 5, max_level)
raw_input()
sys.exit(0)

