import sys
import turtle as t

p = t.Pen()
p.reset()
p.down()
p.speed(100)
pencolour=["green","cyan","blue","violet", "red", "yellow"]
t.pencolor(pencolour[2])

def dragonY(length, level):
	global t
	if level>0:
		t.right(45)
		t.forward(length/2)
		dragonX(length/2,level-1)
		t.right(45)
		dragonY(length/2,level-1)
	#else:
	#	t.forward(length/2)
def dragonX(length, level):
	global t
	if level>0:
		dragonX(length/2,level-1)
		t.left(45)
		dragonY(length/2,level-1)
		t.forward(length/2)
		t.left(45)
	#else:
	#	t.forward(length/2)
	
dragonX(100, 5)
raw_input()
sys.exit(0)


