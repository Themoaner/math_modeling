import matplotlib.pyplot as plt 
import numpy as np 

R=0.5
t = np.arange(-R, 4*np.pi, 0.1) #parametr

x = R * (np.cos(t))**3
y = R * (np.sin(t))**3
plt.plot(x, y, ls='--', lw=3)

plt.axis('equal')

plt.show()