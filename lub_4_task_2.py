def my_func(A):
  b=1
  for i in range(len(A)):
    c=b*A[i]
    b=c
    print(c)

my_func([1,2,3,4,5])
