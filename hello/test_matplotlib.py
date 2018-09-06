'''
Created on 2018/04/08

@author: syuu
'''
import numpy
from matplotlib import pyplot

t = numpy.arange(0.,5.,0.2)

pyplot.title("drawing example1")


pyplot.plot(t,t,'r--',label='linear')
pyplot.plot(t,t**2,'bs',label='square')
pyplot.plot(t,t**3,'g^',label='cube')

pyplot.xlabel("x values")
pyplot.ylabel("y values")

pyplot.legend()
pyplot.show()