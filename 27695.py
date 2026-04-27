import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


mod = 10 ** 9 + 9
f = [1, 1] + [0] * 99999
for i in range(2, 100001):
    f[i] = f[i-1] * i % mod


def nCk(n, k):
    num = f[n]
    den = f[k] * f[n - k] % mod
    ret = num * pow(den, -1, mod) % mod
    return ret


for _ in range(int(input_())):
    input_()
    n = int(input_()) + 1
    if n & 1:
        print(((n + 1) * pow(2, n - 2, mod) - n * nCk(n - 1, (n - 1) >> 1)) % mod)
    else:
        print(((n + 1) * pow(2, n - 2, mod) - 2 * (n - 1) * nCk(n - 2, (n - 2) >> 1)) % mod)
