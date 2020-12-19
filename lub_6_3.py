import matplotlib.pyplot as plt 
import numpy as np 

def plotter(a=10,b=5,radius=10,title='plotter'):
  x=np.arange(-20,20,0.1)
  y=np.arange(-20,20,0.1)

  X,Y = np.meshgrid(x,y)
  fxy= X**2 + Y**2
  plt.contour(X, Y, fxy, levels=[radius**2])

  fxy2= X**2/a**2 + Y**2/b**2
  plt.contour(X, Y, fxy2, levels=[1])
  plt.axis('equal')
  plt.show()

plotter()