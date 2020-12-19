import matplotlib.pyplot as plt 
import numpy as np 

plt.plot([1,1,5,5,1],[1,5,5,1,1],label='квадрат', marker='o', ms=5)
plt.legend()
plt.axis('equal')
plt.show()
