import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')

def circle_move(phi, angle_vel ,t):
  alpha = angle_vel * (np.pi/180) * t
  R = alpha * t
  x = R*np.cos(phi)
  y = R*np.sin(phi)
  return x,y

edge=100
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  ball.set_data(circle_move(angle_vel=1, phi=np.linspace(0, 2*np.pi, 100), t=i))

ani = FuncAnimation(fig, animate, frames=100, interval=30)

ani.save('lub_7_2.gif')