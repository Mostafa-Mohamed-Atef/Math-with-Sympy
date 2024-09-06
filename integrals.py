from sympy import *
init_printing(use_unicode=False)
problem = input("Enter Your Problem: \n")
respect_to = symbols(input("With Respect to: \n"))
integration = diff(sympify(problem), sympify(respect_to))
print(f"Answer => {integration} + c")