from sympy import *

x, y, z = symbols('x y z')
problem = input("Enter Your Problem: \n")
approach = int(input("x->"))
limit_result = limit(sympify(problem),x,approach)
print(limit_result)
