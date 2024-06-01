
from math import *
NT = float

#from pylab import *
#from matplotlib.matlab import *
#from matplotlib.pylab import *


xconst = 0.2
yconst = 0.2

PI=3.14
xline=0.1
m=2.0
c=10.0
n=36
r=20.0
xc=0.0
yc=0.0
theta=0.0
angle_quantum=2*PI/n
for i in range(2*n):
    x=[]
    y=[]
    xline=xline+0.5
    yline=m*xline+c
#    xline=0.0
#    yline=0.0
    x.append(xline)
    y.append(yline)

    xcircle=r*cos(theta)+xc
    ycircle=r*sin(theta)+yc
    theta = theta + angle_quantum
    x.append(xcircle)
    y.append(ycircle)

    plot(x,y)
show()
