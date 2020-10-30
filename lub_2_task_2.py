#lub_2_task_2
b = int(input('введите b '))
q = int(input('введите q '))
n = int(input('введите n '))
a = b * q**(n-1)
for i in range(0, n, 1):
  a = b * q**(i)
  print(a)
