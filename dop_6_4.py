import matplotlib.pyplot as plt 
import numpy as np 

def plotter(N=1, x=0, y=0, title='lesenka'):
  x=np.arange(0, 10, 0.1)
  y=x

  if x==(x[N],x[N+1]):
    y=N

  
  plt.plot(x,y,label='stupenki')
  plt.xlabel('coord - x')
  plt.ylabel('coord - y')
  plt.title(title)
  plt.grid()
  plt.legend()
  plt.show()

plotter()