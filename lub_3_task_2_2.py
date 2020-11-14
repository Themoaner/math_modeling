from numpy import pi
from lub_3_task_1 import Boltzmann_constant as k
from lub_3_task_1 import euler_number as e 
from lub_3_task_1 import Plancks_constant as h
T = 200
E = 300
N = (2/(pi)**0.5) * (h/(k*T)**3/2) * e**(-E/(k*T)) * E**(T/2)
print(N)