import numpy as np
# import time

# Defining a function that adds two matrices
def MatrixAddition(matrix_a, matrix_b):
    m,n = matrix_a.shape
    matrix_c = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            matrix_c[i][j] += matrix_a[i][j] + matrix_b[i][j]
    return np.array(matrix_c)

# Defining a function that multiplies two matrices 
def MatrixMultiplication(matrix_a, matrix_b):
    m,n = matrix_a.shape
    n,p= matrix_b.shape
    matrix_c = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                matrix_c[i][j] += matrix_a[i][k]*matrix_b[k][j]
    return np.array(matrix_c)

# Taking the shape-input from user...
a = int(input("Enter how many rows: "))
b = int(input("Enter how many columns: "))

print("\n")

# Asking the user to initialize the elements of the matrices...
print("Enter the elements of the first matrix please")
first_matrix = [[0 for i in range(a)] for j in range(b)]
for i in range(a):
    for j in range(b):
        first_matrix[i][j] += int(input("first_matrix["+str(i)+"]["+str(j)+"]: "))
first_matrix = np.array(first_matrix)

print("Now enter the elements of the second matrix please")

second_matrix = [[0 for i in range(a)] for j in range(b)]
for i in range(a):
    for j in range(b):
        second_matrix[i][j] += int(input("second_matrix["+str(i)+"]["+str(j)+"]: "))
second_matrix = np.array(second_matrix)

print("\n")

# Printing the matrices!
print("The first matrix given is: \n", first_matrix)
print("The second matrix given is: \n", second_matrix)

resultant_sum_matrix = MatrixAddition(first_matrix, second_matrix)
print("The sum of the given matrices is:")
# time.sleep(0.5)
print(resultant_sum_matrix)

resultant_product_matrix= MatrixMultiplication(first_matrix, second_matrix)
print("The product of the given matrices is: ")
# time.sleep(0.5)
print(resultant_product_matrix)
