import sys
import turtle as t

p = t.Pen()
p.reset()
p.down()
p.speed(999999)
pencolour=["green","cyan","blue","violet", "red", "yellow"]
t.pencolor(pencolour[2])

def draw_h(t, length, level):
	if level>0:
		t.forward(length)
		t.right(90)
		t.forward(length)
		draw_h1(t, length/2, level-1)
		t.right(180)
		t.forward(length)
		t.forward(length)
		draw_h1(t, length/2, level-1)
		t.right(180)
		t.forward(length)
		t.right(90)
		t.forward(length)

def draw_h1(t, length, level):
	draw_h(t, length, level)
	draw_h(t, length, level)
	
draw_h1(t, 100, 5)
raw_input()
sys.exit(0)


