from numpy import pi

def my_func(p,a=2,b=3,h=4,R=5):
  """  
  1-круг (введите R)
  2-прямоугольник (введите a,b)
  3-треугольник (введите a,h)
  """
  if p==1:
    x=pi*R**2
    print(x)
  elif p==2:
    x=a*b
    print(x)
  elif p==3:
    x=(a*h)/2
    print(x)

my_func()
