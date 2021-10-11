import numpy as np

a = np.matrix([[1, -2, 1], [3, 2, 2], [2, -1, 1]])
b = np.matrix([[1], [-2], [2]])

x = [0, 0, 0]

def f():

    k = 0
    n = len(b)-1

    while k <= n - 1:

        i = k + 1
        while i <= n:

            j = k
            while j <= n:

                a[i, j] = a[i, j] - (a[i, k] / a[k, k]) * a[k, j]
                j += 1

            b[i] = b[i] - (a[i, k] / a[k, k]) * b[k]
            i += 1

        k += 1

    x.insert(n + 1, b[n, 0] / a [n, n])
    x.pop(n)

    i = n

    while i >= 0:

        j = i + 1
        sum = 0
        while j <= n:

            sum = sum + a[i, j] * x[j]
            j += 1

        x.insert(i + 1, (b[i, 0] - sum) / a[i, i])
        x.pop(i)

        print(x[i])

        i -= 1

print('\nmethod of Gauss:')
f()

print('\ncheck of the solution:\n', np.linalg.solve(a, b))
print('\nmethod of Jordan-Gauss:\n', np.linalg.inv(a)*b, '\n')

