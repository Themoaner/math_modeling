import matplotlib.pyplot as plt 
import numpy as np 
from np import pi
from np import cos
from np import sin

def plotter(a=1,b=0.1,r=1,f=30, title='plotter'):
  f = np.arange(0.01, 8*pi, 0.1)
  r = a/f**0.5

  x=r*cos(f)
  y=r*sin(f)
 
  plt.plot(x,y)
  plt.axis('equal')
  plt.show()

plotter()