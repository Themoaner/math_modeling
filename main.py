print('Hello World!')
print('маша + петя = любовь')
x = 3 + 4
print(x)


print(type('Hello world!'))
print(type('x=3+4'))
print(type('3/4'))
print(type([1, 2, 5, 10, 100]))


a = [1, 5, 'Good', 'Bad']
b = [9, 'Blue', 'Red', 11]

c = a + b
print(c)


a = int(input('введите а'))
if a % 2 == 0:
  print('чётное')
else:
  print('нечётное')