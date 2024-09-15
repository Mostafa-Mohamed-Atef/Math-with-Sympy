from sympy import Matrix

input_matrix = [list(map(int, input().strip().split(" "))) for _ in range(2)]
M = Matrix(input_matrix)
det = M.det()  
inv = M.inv()  
eigenvals = M.eigenvals()  
print(f"Determinant => {det}\n", f"Inverse => {inv}\n", f"Eigenvalues => {eigenvals}")
