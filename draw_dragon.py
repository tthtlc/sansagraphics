import sys
import string
import turtle as t
from dragon_string import *

p = t.Pen()
p.reset()
p.down()
p.speed(100)
pencolour=["green","cyan","blue","violet", "red", "yellow"]
t.pencolor(pencolour[2])

myarray=dragon(2)
for i in range(len(myarray)):
	#print myarray[i]
	if (myarray[i]=='0'):
		t.left(30)
	else:
		t.right(30)
	t.forward(10)
		
#print myarray
raw_input()
sys.exit(0)


