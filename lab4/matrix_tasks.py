import numpy as np
import copy
import random

# task 1. find matrix AB - BA
# var. 2

a = np.matrix([[2, 3, 1], [-1, 1, 0], [1, 2, -1]])
b = np.matrix([[1, 2, 1], [0, 1, 2], [3, 1, 1]])

print ('\nTask 1. Var 2. A*B - B*A: \n\n', a*b - b*a)
print ('_' * 70)

#--------------------------------------------------------------------------------
# task 2. exponentiate the matrix
# var. 2

c = np.matrix([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])

print('Task 2. Var 2. Matrix C squared: \n\n', np.linalg.matrix_power(c, 2))
print ('_' * 70)

#--------------------------------------------------------------------------------
# task 3. find the product of matrices
# var. 4

d = np.matrix([[5, 0, 2, 3], [4, 1, 5, 3], [3, 1, -1, 2]])
e = np.matrix([[6], [-2], [7], [4]])

print ('Task 3. Var 4. D*E: \n\n', d*e)
print ('_' * 70)

#--------------------------------------------------------------------------------
# task 4. find the determinant
# var. 5

f = np.matrix([[1, 5, -5], [4, 0, 3], [2, -10, 3]])
print ('Task 4. Var 5. \n')
print ('determinant: ', np.linalg.det(f))
print ('determinant rounded: ', round(np.linalg.det(f)) )
print ('_' * 70)

#--------------------------------------------------------------------------------
# task 5. find the determinant
# var. 2

g = np.matrix([[2, 3, 4, 1], [1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]])
print ('Task 5. Var 2. \n')
print ('determinant: ', np.linalg.det(g))
print ('determinant rounded: ', round(np.linalg.det(g)) )
print ('_' * 70)

#--------------------------------------------------------------------------------
# task 6. transpose the matrix
# var. 5

h = np.matrix([[2, 1, 0, 0], [3, 2, 0, 0], [1, 1, 3, 4], [2, -1, 2, 3]])
print ('Task 6. Var 5. Matrix H transponed: \n\n', h.getT())
print ('_' * 70)

#--------------------------------------------------------------------------------
# task 7. find matrix rank
# var. 3

i = np.matrix([[1, -1, 3, 4], [0, -1, 2, 1], [1, 1, -1, 2], [2, 3, -5, 3]])
print ('Task 7. Var 3.\n\nMatrix I rank: ', np.linalg.matrix_rank(i))
print ('_' * 70)

#--------------------------------------------------------------------------------
# task 8. solve the system of equations by Cramer's rule
# var. 4

q = np.matrix([[7, 3, -6], [7, 9, -9], [2, -4, 9]])
r = np.matrix([[-1, 5, 28]])

dets = []

det_q = np.linalg.det(q)

qi = copy.copy(q)

for i in range(len(qi)):

    for j in range(len(qi)):

        qi[j, i] = r[0, j]

    det_qi =  np.linalg.det(qi)
    dets.append(det_qi)
        
    qi = copy.copy(q)

print ('Task 8. Var 4.\n')

print('Determinants:\n')
print(dets)

print("\nSolution by Cramer's rule:\n")

for i in range(len(q)):
    xi = dets[i]/det_q
    print(f'x{i+1} = {xi}')

print ('_' * 70)

#--------------------------------------------------------------------------------
# task 9. solve the system of equations by the matrix method
# var. 5

j = np.matrix([[4, 1, 4], [1, 1, 2], [2, 1, 2]])
k = np.array([[-2], [-1], [0]])

det_j = round(np.linalg.det(j))

print("Task 9. Var 5.")

if (det_j == 0):
    print ("\nThere's no solution")

else:
    print ("\nSolution by matrix method: ")
    x1 = np.linalg.inv(j) * k
    print(x1)

    print ("\nCheck of the solution: ")
    x2 = np.linalg.solve(j,k)
    print(x2)

print ('_' * 70)

#--------------------------------------------------------------------------------
# task 10. solve the task
# var. 4

# Створіть прямокутну матрицю A,
# яка має N рядків і M стовпців
# з випадковими елементами.
# Знайдіть суму елементів всієї матриці.
# Визначте, яку долю в цій сумі складає
# сума елементів кожного стовпця.

def task10():

    print("Task 10. Var 4.\n")

    print('Enter the number of raws: ')
    n = int(input())

    print('Enter the number of columns: ')
    m = int(input())

    a = np.zeros((n, m))

    lim = n*m

    a0 = []

    i = 0

    while i < lim:

        a0.append(random.randint(0, 100))
        i+=1

    k = 0

    for i in range(n):
        for j in range(m):
            a[i, j] = a0[k]
            k+=1
            
    print('\nMatrix of random numbers: \n')
    print(a)

    sum = 0

    for raw in a:
        for elem in raw:
            sum = sum + elem

    print('\nSum of the elements:')
    print(sum)

    for i in range(m):
        sumcol = 0
        for j in range(n):
            sumcol = sumcol + a[j, i]
            part = sumcol/sum
        print(f'\nSum of column {i+1}:')
        print(sumcol)
        print('Part in the general sum:')
        print(part)

task10()

print ('_' * 70)