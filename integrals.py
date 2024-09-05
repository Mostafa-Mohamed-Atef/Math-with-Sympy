from sympy import *
init_printing(use_unicode=False)
equation = input("Enter your function: \n")
x = Symbol('x')
integration = integrate(sympify(equation))
print(f"{integration} + c")