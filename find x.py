from sympy import *
x, y, z = symbols('x y z')
num_of_equations = int(input("Enter Number of Equations: \n"))
equations = []
for _ in range(num_of_equations):
    equation = input("Enter your Equation: \n").strip()
    left, right = equation.split("=")
    eq = Eq(sympify(left), sympify(right))
    equations.append(eq)

solution = solve(equations)
print(solution)