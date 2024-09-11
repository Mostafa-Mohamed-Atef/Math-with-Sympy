from sympy import *

x = symbols('x')
taylor = series(exp(x), x, 0, 6)
print(taylor)
