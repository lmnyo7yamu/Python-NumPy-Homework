import numpy as np


matrix_A = np.random.randint(0, 10, (4, 4))
matrix_B = np.eye(4)

print("Matrix A:")
print(matrix_A)
print("\nMatrix B:")
print(matrix_B)
print("-" * 20)


print("a) Sum of A and B:")
print(matrix_A + matrix_B)


total_sum = np.sum(matrix_A) + np.sum(matrix_B)
print("\nb) Sum of all elements in A and B:", total_sum)


print("\nc) Maximum value in matrix A:", np.max(matrix_A))


A_reshaped = matrix_A.reshape(8, 2)
B_reshaped = matrix_B.reshape(2, 8)
multiplication_result = np.dot(A_reshaped, B_reshaped)
print("\nd) Result of multiplication after reshaping:")
print(multiplication_result)


col_sum = np.sum(matrix_A[:, 2])
row_sum = np.sum(matrix_B[2, :])
print("\ne) Sum of 3rd column of A and 3rd row of B:", col_sum + row_sum)


A_squared = matrix_A.copy()
A_squared[:, 1] = A_squared[:, 1] ** 2
print("\nf) Matrix A with 2nd column values squared:")
print(A_squared)


horizontal_join = np.hstack((matrix_A, matrix_B))
print("\ng) Horizontally joined matrix (A and B):")
print(horizontal_join)


A_str = matrix_A.astype(str)
B_str = matrix_B.astype(str)
string_addition = np.char.add(A_str, B_str)
print("\nh) String addition of A and B:")
print(string_addition)

m1 = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
m2 = np.array([[3, 4, 5], [6, 7, 8], [9, 10, 11]])


final_result = np.dot(m1, m2.T)

print("\n" + "="*30)
print("QUESTION 2 RESULT:")
print(final_result)
