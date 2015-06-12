import sys
import turtle as t

p = t.Pen()
p.reset()
p.down()
p.speed(100)
pencolour=["green","cyan","blue","violet", "red", "yellow"]
t.pencolor(pencolour[2])

def triangle(t, length, level):
	if level>1:
		t.forward(length/2)
		triangle(t, length/2, level-1)
		t.forward(length/2)
		t.left(60)
		t.forward(length/2)
		triangle(t, length/2, level-1)
		t.forward(length/2)
		t.right(120)
		t.forward(length/2)
		triangle(t, length/2, level-1)
		t.forward(length/2)
		t.left(60)
		t.forward(length/2)
		triangle(t, length/2, level-1)
		t.forward(length/2)
	
triangle(t, 50, 4)
t.right(120)
triangle(t, 50, 4)
t.right(120)
triangle(t, 50, 4)
t.right(120)
raw_input()
sys.exit(0)


