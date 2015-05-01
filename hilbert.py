#!/usr/bin/env python2.7

import numpy
from optparse import OptionParser
import os
import sys
import turtle as t

colorMaps = [m for m in plt.cm.datad if not m.endswith("_r")]

def drawData(ax, data, options):
    if options.matshow:
        plt.matshow(data, fignum=False, origin='upper', cmap=plt.get_cmap(options.cmap))
    else:
        data = data[ ::-1,:] # reverse row order
        plt.pcolor(data, cmap=plt.get_cmap(options.cmap))
    ax.set_xticks([])
    ax.set_yticks([])
    
def d2xy(n, d):
    """
    take a d value in [0, n**2 - 1] and map it to
    an x, y value (e.g. c, r).
    """
    assert(d <= n**2 - 1)
    t = d
    x = y = 0
    s = 1
    while (s < n):
        rx = 1 & (t / 2)
        ry = 1 & (t ^ rx)
        x, y = rot(s, x, y, rx, ry)
        x += s * rx
        y += s * ry
        t /= 4
        s *= 2
    return x, y

def rot(n, x, y, rx, ry):
    """
    rotate/flip a quadrant appropriately
    """
    if ry == 0:
        if rx == 1:
            x = n - 1 - x
            y = n - 1 - y
        return y, x
    return x, y
#
########################################

def genericCurve(options):
    x, y = generateVectors(options.level)
    fig, pdf = initImage(8, 8, options)
    ax = establishAxis(fig, options)
    ax.set_aspect('equal')
    plt.plot(x, y)
    ax.set_xlim([-0.5, (1 << options.level) - .5])
    ax.set_ylim([-(1 << options.level) + .5, 0.5])
    ax.set_xticks([])
    ax.set_yticks([])
    plt.box(on=False)
    writeImage(fig, pdf, options)

def hilbert(t, level):
    data = generateDemo(options)
    drawData(ax, data, options)

def generateVectors(level):
    """
    Given a level, this will generate x and y vectors that
    can be used to plot the hilbert curve path for that level.
    Useful for explaining HCs.
    """
    n = (1 << level)
    x = numpy.zeros(n**2, dtype=numpy.int16)
    y = numpy.zeros(n**2, dtype=numpy.int16)
    for i in xrange(0, n**2):
        x[i], y[i] = d2xy(n, i)
    return x, -y

def generateDemo(options):
    n = 1 << options.level
    m = numpy.zeros((n, n))
    for i in xrange(0, n**2):
        x, y = d2xy(n, i)
        m[y][x] = i
    return m

        #genericCurve(options)
hilbert(t, level)
