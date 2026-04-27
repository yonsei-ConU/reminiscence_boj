mod = 1000000007

def multiply(a, b):
    r = [[0] * len(a) for i in range(len(b[0]))]
    for p in range(len(a)):
        for q in range(len(a[0])):
            for s in range(len(b[0])):
                try:
                    r[p][q] += a[p][s] * b[s][q]
                except IndexError:
                    return r
            r[p][q] %= mod
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

n = int(input())
t = matrix_pow([[1, 1], [1, 0]], n - 1)
r = multiply(t, [[1], [0]])
print(r[0][0])
