import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


mod = 10 ** 9 + 7

f = [1, 1] + [0] * 199999
for i in range(2, 200001):
    f[i] = f[i-1] * i % mod


def nCk(n, k):
    num = f[n]
    den = f[k] * f[n - k] % mod
    ret = num * pow(den, -1, mod) % mod
    return ret


for _ in range(int(input_())):
    N, M = minput()
    ans = nCk(2 * N - 1, N) * nCk((M - N) * 2, M - N + 1) % mod
    if N + 1 == M:
        print(ans)
        continue
    for x in range(N - 1):
        tmp = nCk(N + x, x) * nCk(2 * M - N - 2 - x, M - N - 2)
        ans = (ans + tmp) % mod
    print(ans)
