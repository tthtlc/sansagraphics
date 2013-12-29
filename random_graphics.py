# random circles in Tkinter
# a left mouse click will idle action for 5 seconds
# tested with Python24    vegaseat    14sep2005
from Tkinter import *
import random
import time
##def idle5(dummy):
##    """freeze the action for 5 seconds"""
##    root.title("Idle for 5 seconds")
##    time.sleep(5)
##    root.title("Happy Circles ...")
# create the window form
def idle5(event=None):
    """freeze the action for 5 seconds and save image file"""
    root.title("Idle for 5 seconds")
    time.sleep(5)
    root.title("Happy Circles ...")
  #  cv.postscript(file="circles.eps") # save canvas as encapsulated postscript
  #  child = SP.Popen("circles.eps", shell=True) # convert eps to jpg with ImageMagick
  #  child.wait()
    cv.postscript(file="circles.eps")
    from PIL import Image
    img = Image.open("circles.eps")
    img.save("circles.png", "png")
    print "save"

root = Tk()
# window title text
root.title("Happy Circles ...")
# set width and height
w = 640
h = 480
# create the canvas for drawing
cv = Canvas(width=w, height=h, bg='black')
cv.pack()
# list of colors to pick from
colorList = ["blue", "red", "green", "white", "yellow", "magenta", "orange"]
# endless loop to draw the random circles
while 1:
    # random center (x,y) and radius r
    x = random.randint(0, w)
    y = random.randint(0, h)
    r = random.randint(5, 50)
    # pick the color
    color = random.choice(colorList)
    # now draw the circle
    cv.create_oval(x, y, x+r, y+r, fill=color)
    # update the window
    root.update()
    # bind left mouse click, idle for 5 seconds
    cv.bind('<Button-1>', idle5)
# start the program's event loop
root.mainloop()




