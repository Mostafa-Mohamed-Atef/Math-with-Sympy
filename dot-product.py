from sympy import Matrix

print("Matrix A \n")
a_matrix = [list(map(float, input().strip().split(" "))) for _ in range(2)]
print("Matrix A \n")
b_matrix = [list(map(float, input().strip().split(" "))) for _ in range(2)]
A = Matrix(a_matrix)
B = Matrix(b_matrix)
result = A * B
print(result)
