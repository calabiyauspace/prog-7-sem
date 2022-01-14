from scipy.integrate import quad
import timeit
def integral(x, a, b):
  return x**2
a = 0
b = 0
time = timeit.timeit('quad(integral, 1, 4, args=(a,b))', 'from __main__ import integral, quad, a, b', number=100)
print(time)
