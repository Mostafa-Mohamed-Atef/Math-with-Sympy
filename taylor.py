from sympy import *

x = symbols('x')
problem = input("Enter the function to expand in Taylor series: \n")
order = int(input("Enter the order of expansion: \n"))
taylor_result = series(sympify(problem), x, 0, order)
print(taylor_result)
