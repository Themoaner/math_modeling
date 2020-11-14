from numpy import pi
from numpy import tan
from numpy import cos
from lub_3_task_1 import acceleration_of_gravity as g
h = 100
a = pi/3
b = 30 * (pi/180)
c = g*h * tan(b)**2
d = 2 * cos(a)**2 * (1 - tan(b) * tan(a))
V = (c/d)**0.5
print(V)



