import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


mod = 10 ** 9 + 7

fib = [0, 1, 1, 2]
for i in range(100000): fib.append((fib[-1] + fib[-2]) % mod)

fact = [1, 1] + [0] * 99999
for i in range(2, 100001):
    fact[i] = fact[i-1] * i % mod


def comb_mod(n, k):
    num = fact[n]
    den = fact[k] * fact[n - k] % mod
    ret = num * pow(den, mod - 2, mod) % mod
    return ret


def nHr(n, r):
    return comb_mod(n + r - 1, r)


N, K = minput()
fib[3] = 1

if not K: exit(print(fib[N + 2]))

ans = fib[N + 2]

for k in range(K, N, K):
    print(N - k + 1, k, fib[N - k + 2], nHr(N - k + 1, k))
    ans += fib[N - k + 2] * nHr(N - k + 1, k)
    ans %= mod

print(ans)
