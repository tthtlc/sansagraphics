
from math import *
NT = float

from pylab import *
#from matplotlib.matlab import *
from matplotlib.pylab import *


xconst = 0.2
yconst = 0.2

x=[]
y=[]
for i in range(10):
	x.append(xconst+0.2)
	y.append(yconst+0.2)
	xconst = xconst + 0.3
	yconst = yconst + 0.4

plot(x,y)
show()
