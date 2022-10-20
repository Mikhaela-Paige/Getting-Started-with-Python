import numpy as np
"""
Multiplying two matrices in a clever way -- With a time complexity of O(N^2.8074..) as opposed to the 
brute-force complexity of O(N³).
NOTE: This algorithm only works for square matrices specifically with even shapes (like 2-by-2, 4-by-4, etc.)
"""
# Defining a function to make four quarters of the given matrix
def split_matrix(matrix):
    n_rows, n_cols = matrix.shape
    n_rows_split, n_cols_split = n_rows//2, n_cols//2
    return matrix[:n_rows_split, :n_cols_split], matrix[:n_rows_split, n_cols_split:], matrix[n_rows_split:, :n_cols_split], matrix[n_rows_split:, n_cols_split:]

# Defining the recursive Strasssen's Algorithm...
def Strassens(matrix_a, matrix_b):
    if (len(matrix_a) == 1):
        return matrix_a*matrix_b
    a,b,c,d = split_matrix(matrix_a)
    e,f,g,h = split_matrix(matrix_b)
    p1 = Strassens(a, f-h)
    p2 = Strassens(a+b, h)
    p3 = Strassens(c+d, e)
    p4 = Strassens(d, g-e)
    p5 = Strassens(a+d, e+h)
    p6 = Strassens(b-d, g+h)
    p7 = Strassens(a-c, e+f)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    matrix_c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return np.array(matrix_c)

# Establishing the condition that the matrices given should be square and of even shape.
while(True):
    a = int(input("Enter how many rows: "))
    b = int(input("Enter how many columns: "))
    if ((a == b) & (a%2==0) & (b%2 ==0)):
        break
    else: 
        print("The matrices aren't square!\n\tOR\nIf square, their shapes are not even!\n")
print("-------------------------------------------------------------")
first_matrix = [[0 for i in range(a)] for j in range(b)]
for i in range(a):
    for j in range(b):
        first_matrix[i][j] += int(input("first_matrix["+str(i)+"]["+str(j)+"]: "))
first_matrix = np.array(first_matrix)
print("-------------------------------------------------------------")
second_matrix = [[0 for i in range(a)] for j in range(b)]
for i in range(a):
    for j in range(b):
        second_matrix[i][j] += int(input("second_matrix["+str(i)+"]["+str(j)+"]: "))
second_matrix = np.array(second_matrix)
product_matrix = Strassens(first_matrix, second_matrix)
print("-------------------------------------------------------------")
print("The first matrix given is: \n", first_matrix)
print("The second matrix given is: \n", second_matrix)
print("The product of the two given matrices is: \n", product_matrix)
