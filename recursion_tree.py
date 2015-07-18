import sys
import turtle as t

p = t.Pen()
p.reset()
p.down()
p.speed(100)
pencolour=["green","cyan","blue","violet", "red", "yellow"]
t.pencolor(pencolour[2])

def asym_tree(t, length, level):
	if level>0:
		t.forward(length/2)
		t.right(30)
		t.forward(length/2)
		asym_tree(t, length/2, level-1)
		t.forward(-length/2)
		t.left(60)
		t.forward(length/2)
		asym_tree(t, length/2, level-1)
		t.forward(-length/2)
		t.right(30)
		t.forward(-length/2)
	
asym_tree(t, 200, 5)
raw_input()
sys.exit(0)


