import matplotlib.pyplot as plt 
import numpy as np 

def circle_plotter(radius=10):
  '''рисует окружность заданного радиуса
  '''
  x=np.arange(-2*radius, 2*radius, 0.1)
  y=np.arange(-2*radius, 2*radius, 0.1)

  #переход к неявнозаданным координатам
  X, Y = np.meshgrid(x,y)

  fxy = X**2 + Y**2#уравнение окружности

#команда рисования
  plt.contour(X, Y, fxy, levels=[radius**2])
  plt.axis('equal')
  plt.show()

circle_plotter()