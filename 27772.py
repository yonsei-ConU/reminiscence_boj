import sys
from math import gcd, isqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    N, T = minput()
    L = list(minput())
    L_real = [0] * (T + 1)
    for i in range(T - 1):
        if L[i] == L[i + 1]:
            continue
        else:
            L_real[i + 1] = gcd(L[i], L[i + 1])
            L_real[i] = L[i] // L_real[i + 1]
            L_real[i + 2] = L[i + 1] // L_real[i + 1]
            break
    else:
        print(10 ** 10000)  # ValueError
    for j in range(i + 3, T + 1):
        L_real[j] = L[j - 1] // L_real[j - 1]
    for k in range(i - 1, -1, -1):
        L_real[k] = L[k] // L_real[k + 1]
    primes = sorted(set(L_real))
    rank = {primes[i]: i for i in range(len(primes))}
    ans = []
    for i in range(T + 1):
        ans.append(chr(rank[L_real[i]] + 65))
    print(f"Case #{tc}: {''.join(ans)}")
