import matplotlib.pyplot as plt 
import numpy as np 

R=0.5
t = np.arange(-R, 4*np.pi, 0.1) #parametr

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))
plt.plot(x, y, ls='--', lw=3)

plt.axis('equal')

plt.show()