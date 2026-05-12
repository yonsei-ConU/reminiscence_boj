import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
MOD = 1000000007


def comb(n, k):
    nu = fact_mod[n]
    de = fact_mod[k] * fact_mod[n-k] % MOD
    return nu * pow(de, MOD - 2, MOD) % MOD


fact_mod = [1, 1] + [0] * 299999
for i in range(2, 300001):
    fact_mod[i] = fact_mod[i-1] * i % MOD


