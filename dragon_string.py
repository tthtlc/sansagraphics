import sys
#import string
#import turtle as t

#p = t.Pen()
#p.reset()
#p.down()
#p.speed(100)
#pencolour=["green","cyan","blue","violet", "red", "yellow"]
#t.pencolor(pencolour[2])

def complement_middle(mystring_array):
	mylen=len(mystring_array)/2
	if mystring_array[mylen]=='1':
		newstring='0'
	elif mystring_array[mylen]=='0':
		newstring='1'
	if (mylen>0):
		return mystring_array[:mylen-1] + newstring + mystring_array[mylen+1:]
	else:
		return newstring
	
def dragon(level):
	if level>0:
		newstring=complement_middle(dragon(level-1))
		print dragon(level-1) + "1" + newstring
		return dragon(level-1) + "1" + newstring
	else:
		return '1'
	
myarray=dragon(10)
#print myarray
#raw_input()
#sys.exit(0)


