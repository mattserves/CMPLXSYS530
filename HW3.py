# HW3 based on CT Turing Pattern FOrmation in PyCX

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 50
height = 50
populationSize = 1
agentx = 0
agenty = 0
directionx = [0, 1, 0, -1]
directiony = [1, 0, -1, 0]
heading = RD.randint(0,3)


def init():
    global time, agentx, agenty, envir

    time = 0
    
    xstart = RD.randint(0, width - 1)
    ystart = RD.randint(0, height - 1)

    agentx = xstart
    agenty = ystart   
    

    
    envir = SP.zeros([height, width])
    for x in xrange(width):
        for y in xrange(height):
            envir[y, x] = 0

   
def draw():
    PL.cla()
    PL.pcolor(envir, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.hold(True)
    x = [agentx]
    y = [agenty]
    PL.scatter(x, y, cmap = PL.cm.binary)
    PL.hold(False)
    PL.title('t = ' + str(time))

def step():
    global time, agentx, agenty, envir, heading, directionx, directiony

    time += 1
    
    if envir[agenty,agentx] == 0:
       if heading > 0:
           heading = heading - 1
       else:
           heading = heading + 3
           
       envir[agenty,agentx] = 1


    else:
        if heading < 3:
           heading = heading + 1
        else:
           heading = heading - 3
           
        envir[agenty,agentx] = 0
        
    agentx = agentx + directionx[heading]
    agenty = agentx + directiony[heading]
    

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
