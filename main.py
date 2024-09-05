from sympy import *
init_printing(use_unicode=False)
x = Symbol('x')
print(integrate(4*x**3 + 2*x, x))