mod = 1000000007

def multiply(a, b):
    r = [[0] * len(a) for i in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b[0])):
                try:
                    r[i][k] += (a[i][j] * b[j][k]) % mod
                except IndexError:
                    return r
            r[i][k] %= mod
    return r

def matrix_pow(a, b):
    if b <= 1:
        for x in range(len(a)):
            for y in range(len(a)):
                a[x][y] %= mod
        return a
    if not b % 2:
        t = matrix_pow(a, b // 2)
        return multiply(t, t)
    else:
        t = matrix_pow(a, b - 1)
        return multiply(t, a)

for i in range(int(input())):
    n = int(input())
    if n <= 5:
        print([1, 3, 10, 23, 62][n-1])
    else:
        t = matrix_pow([[1, 2, 6, 1, 0, -1], [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]], n - 5)
        r = multiply(t, [[62], [23], [10], [3], [1], [1]])
        print(r[0][0])
