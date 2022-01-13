import scipy.integrate as integrate
from scipy.integrate import quad
def integrand(x, a, b):
  return x**2
a = 0
b = 0
I = quad(integrand, 1, 4, args=(a,b))
print(I)