import matplotlib.pyplot as plt 
import numpy as np 

def plotter(a=1,b=1,c=1,title='plotter'):
  x = np.linspace(-11,10,100)
  y1 = a*x**2 + b*x + c
  y2 = a/x
  plt.plot(x,y1,label='parabola')
  plt.plot(x,y2,label='giperbola')
  plt.xlabel('coord - x')
  plt.ylabel('coord - y1, y2')
  plt.title(title)
  plt.grid()
  plt.legend()
  plt.show()

plotter(10,10,10)