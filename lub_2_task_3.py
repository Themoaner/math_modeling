#lub_2_task_3
a = int(input('введите a '))
if a % 400 == 0:
  print('високосный')
elif a % 100 == 0:
  print('невисокосный')
elif a % 4 == 0:
  print('високосный')
else:
  print('невисокосный')
