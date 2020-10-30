#lub_2_task_5
a = int(input('введите a '))
b = int(input('введите b '))
if b == 0:
  print('делить на ноль нельзя')
if a % b == 0:
  print('делится')
  print('частное', a//b)
else:
  print('не делится')
  print('частное', a//b)
  print('остаток', a%b)