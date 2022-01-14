import quad
import timeit
def integral(x, a, b):
  return x**2
a = 0
b = 0
time = timeit.timeit(quad(integral, 1, 4, args=(a,b)), setup , number=100)
print(I)