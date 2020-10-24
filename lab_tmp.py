print('Hello World!')
print('маша + петя = любовь')
x = 3 + 4
print('x=', x)


print(type('Hello world!'))
print(type('x=3+4'))
print(type('3/4'))
print(type([1, 2, 5, 10, 100]))

x = 3
a = x** 1.5
b = x**3 + 3/x
c = 4*x**7 - x**5
d = 80
e = (27*x**4 + 12*x**3 - 5*x**2 + 10)
y = a/b * c + d*e**0.5
print(y)


a = [1, 5, 'Good', 'Bad']
b = [9, 'Blue', 'Red', 11]

c = a + b
print(c)


a = int(input('введите а'))
if a % 2 == 0:
  print('чётное')
else:
  print('нечётное')