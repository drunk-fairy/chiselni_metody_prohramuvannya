import numpy as np

# task 1. find matrix AB - BA
# var. 2
a = np.matrix([[2, 3, 1], [-1, 1, 0], [1, 2, -1]])
b = np.matrix([[1, 2, 1], [0, 1, 2], [3, 1, 1]])

print ('\nTask 1. A*B - B*A: \n\n', a*b - b*a)
print ('_' * 40)

# task 2. exponentiate the matrix
# var. 2
c = np.matrix([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])

print('Task 2. Matrix C squared: \n\n', np.linalg.matrix_power(c, 2))
print ('_' * 40)

# task 3. find the product of matrices
# var. 4

d = np.matrix([[5, 0, 2, 3], [4, 1, 5, 3], [3, 1, -1, 2]])
e = np.matrix([[6], [-2], [7], [4]])

print ('Task 3. D*E: \n\n', d*e)
print ('_' * 40)

# task 4. find the determinant
# var. 5

f = np.matrix([[1, 5, -5], [4, 0, 3], [2, -10, 3]])
print ('Task 4. \n')
print ('determinant: ', np.linalg.det(f))
print ('determinant rounded: ', round(np.linalg.det(f)) )
print ('_' * 40)

# task 5. find the determinant
# var. 2

g = np.matrix([[2, 3, 4, 1], [1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]])
print ('Task 5. \n')
print ('determinant: ', np.linalg.det(g))
print ('determinant rounded: ', round(np.linalg.det(g)) )
print ('_' * 40)

# task 6. transpose the matrix
# var. 5
h = np.matrix([[2, 1, 0, 0], [3, 2, 0, 0], [1, 1, 3, 4], [2, -1, 2, 3]])
#h = np.matrix([[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]])
print ('Task 6. Matrix H transponed: \n\n', h.getT())
print ('_' * 40)

# task 7. find matrix rank
# var. 3

i = np.matrix([[1, -1, 3, 4], [0, -1, 2, 1], [1, 1, -1, 2], [2, 3, -5, 3]])
print ('Task 7.\n\nmatrix I rank: ', np.linalg.matrix_rank(i))
print ('_' * 40)

# task 9. Solve the equation by the matrix method
# var. 4

coeff = np.array([[2, -1, 1], [3, 4, -2], [1, -3, 1]])
const = np.array([5, -3, 4])
print(np.linalg.solve(coeff, const))
