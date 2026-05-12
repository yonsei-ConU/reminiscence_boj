import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='ascii')
input_ = reader.readline
sinput = text_reader.readline
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


output = []
N, MOD = minput()
AB = [list(minput()) for _ in range(N)]
ans = 0
power_10 = 1
for i in range(N - 1, -1, -1):
    mat = [[10, 0], [AB[i][0], 1]]
    ans = (ans + matrix_pow(mat, AB[i][1], MOD)[1][0] * power_10) % MOD
    power_10 = power_10 * pow(10, AB[i][1], MOD) % MOD

output.append(str(ans))

os.write(1, '\n'.join(output).encode())
os._exit(0)
