from numpy import pi

print('Введите фигуру (круг(c), прямоугольник(r), треугольник(t)) : ')
p = str(input( ))

if p=='c':
  def my_func(R):
    x=pi*R**2
    print(x)
elif p=='r':
  def my_func(a, b):
    x=a*b
    print(x)
elif p=='t':
  def my_func(a, h):
    x=(a*h)/2
    print(x)

my_func(int(input( )))