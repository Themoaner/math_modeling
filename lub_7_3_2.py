import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots( ) #создание пространства и подпространства

anim_object, = plt.plot([], [], '-', color='aqua', lw=2) #объект анимации

xdata, ydata = [], [] #координаты объекта анимации

ax.set_xlim(-20, 20) #пределы изменения
ax.set_ylim(-20, 20)

def update(frame):
  xdata.append(16 * (np.sin(frame)**3))
  ydata.append(13*np.cos(frame)-5*np.cos(2*frame)-2*np.cos(3*frame)-np.cos(4*frame))
  anim_object.set_data(xdata, ydata)
  return anim_object,

ani = FuncAnimation(fig, update, frames=np.arange(0, 2*np.pi, 0.1), interval=100)

ani.save('lub_7_3_2.gif')