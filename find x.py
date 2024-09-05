from sympy import *
l, r = input("your equation: \n").strip().split("=")
eqx = Eq(sympify(l),sympify(r))
print(solve(eqx))