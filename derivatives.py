from sympy import *
problem = input("Enter Your Problem: \n")
respect_to = symbols(input("With Respect to: \n"))
diff_degree = int(input("Derivative Degree: \n"))
for i in range(diff_degree):
    if i==0:
        derivative = diff(sympify(problem), sympify(respect_to))
    else:
        derivative = diff(sympify(derivative), sympify(respect_to))


print(f"Answer => {derivative}")