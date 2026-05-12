import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def matrix_mult(a, b, mod):
    r = [[0] * len(b[0]) for _ in range(len(a))]
    for p in range(len(a)):
        for q in range(len(b[0])):
            for s in range(len(a[0])):
                r[p][q] += a[p][s] * b[s][q]
            r[p][q] %= mod
    return r


def matrix_pow(base, exponent, mod):
    ret = []
    for i in range(len(base)):
        lst = [0] * len(base)
        lst[i] = 1
        ret.append(lst)
    while exponent:
        if exponent & 1:
            ret = matrix_mult(ret, base, mod)
        exponent >>= 1
        base = matrix_mult(base, base, mod)
    return ret


N, B = minput()
mat = [list(minput()) for _ in range(N)]
result = matrix_pow(mat, B, 1000)
for r in result:
    print(*r)
