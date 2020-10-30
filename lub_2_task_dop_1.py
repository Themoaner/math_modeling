#lub_2_task_dop_1
a = int(input( ))
b = int(input( ))
c = int(input( ))
d = b**2 - 4*a*c
x1 = ((-b) + d**0.5)/ (a*2)
x2 = ((-b) - d**0.5)/ (a*2)
if d>0:
  print(x1)
  print(x2)
if d==0:
  print(x1)
if d<0:
  print('нет корней')
