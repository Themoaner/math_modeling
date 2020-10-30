#lub_2_task_4
n = int(input( ))
a = 0
b = 1
c = 0
for i in range(0, n, 1):
  c = a
  a = b
  b = c + a
  print(a, sep = '')
