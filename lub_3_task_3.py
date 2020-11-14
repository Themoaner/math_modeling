from numpy import pi
from numpy import cos, sin
from lub_3_task_1 import acceleration_of_gravity as g 
import numpy as np
x_0 = 0
y_0 = 0
t = np.linspace(0, 5, 100)
v_0 = 15
a = 30 * (pi/180)
x = x_0 + (v_0 * cos(a)*t)
y = y_0 + (v_0 * sin(a)* t) - ((g * t**2)/2)
A = np.zeros((100, 3))
for i in range(100):
  A[i, 0] = t[i] 
  A[i, 1] = x[i]
  A[i, 2] = y[i]
print(A)