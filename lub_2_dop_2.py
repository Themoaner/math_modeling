a = int(input('введите a '))
b = int(input('введите b '))
c = int(input('введите c '))

if (a==b==c):
    print('есть треугольник')
    print('равносторонний')
elif a==b or a==c or b==c and (a+b)>c and (a+c)>b and (b+c)>a:
    print('есть треугольник')
    print('равнобедренный')
elif (a+b)>c and (a+c)>b and (b+c)>a:
    print('есть треугольник')
    print('разносторонний')
else:
    print('нет треугольника')
    