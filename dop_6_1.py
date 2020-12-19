import matplotlib.pyplot as plt 
import numpy as np 
from np import pi
from np import sin

def plotter(A=1,B=1,a=7,b=5,title='Кривые Лиссажу'):
  t=np.linspace(0.1,10,1000)
  d=pi/2
  x=A*sin(a*t+d)
  y=B*sin(b*t)

  plt.plot(x,y)
  plt.title(title)
  plt.legend()
  plt.show()

plotter()