__author__ = 'student'
import math
import pylab
from matplotlib import mlab

#xmin = -20.0
#xmax = 20.0
tmin = -math.pi
tmax = math.pi
dt = 0.01
#dx = 0.01
#xlist = mlab.frange (xmin, xmax, dx)
tlist = mlab.frange (tmin, tmax, dt)
pylab.ion()

for a in range (50):
        xlist = [math.sin (t+a/20) for t in tlist]
        ylist = [math.cos (2*t) for t in tlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()
        pylab.pause(0.003)


pylab.close()