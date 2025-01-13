from sympy import *
x, y, z = symbols('x y z')
def calculate(num_of_equations):
    equations = []
    for _ in range(num_of_equations):
        equation = input("Enter your Equation: \n").strip()
        left, right = equation.split("=")
        eq = Eq(sympify(left), sympify(right))
        equations.append(eq)
    return solve(equations)

if __name__=="__main__":
    num_of_equations = int(input("Enter Number of Equations: \n"))
    calculate(num_of_equations)
    print(solution)

