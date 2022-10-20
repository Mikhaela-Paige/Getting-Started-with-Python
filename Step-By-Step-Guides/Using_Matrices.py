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
rows = int(input("Enter how many rows: "))
columns = int(input("Enter how many columns: "))

# Asking the user to initialize the elements of the first matrix...
print("Please write the elements of the matrix in a single line and separated by a space: ")  
elements = list(map(int, input().split()))  
matrix = np.array(elements).reshape(rows, columns)  

# Asking the user to initialize the elements of the second matrix...
rows2 = int(input("Give the number of rows:"))  
columns2 = int(input("Give the number of columns:")) 
print("Please write the elements of the matrix in a single line and separated by a space: ")  
elements2 = list(map(int, input().split()))  
matrix2 = np.array(elements2).reshape(rows2, columns2)  

# Printing the initial matrices...
print("The first matrix given is: \n", matrix)
print("The second matrix given is: \n", matrix2)

# Printing the calculated matrices...
if rows == columns and rows2 == columns2:
    resultant_sum_matrix = MatrixAddition(matrix, matrix2)
    print("The sum of the given matrices is:")
    # time.sleep(0.5)
    print(resultant_sum_matrix)
else:
    print("Only square matrices may be added at this time")

if rows == columns and rows2 == columns2:
    resultant_product_matrix= MatrixMultiplication(matrix, matrix2)
    print("The product of the given matrices is: ")
    # time.sleep(0.5)
    print(resultant_product_matrix)
else:
    print("Only square matrices may be multiplied at this time")
