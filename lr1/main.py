from scipy.integrate import quad
def integral(x, a, b):
  return x**2
a = 0
b = 0
I = quad(integral, 1, 4, args=(a,b))
print(I)