import sys
from math import gcd
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


S = input_().rstrip()
N = len(S)
divisors = []
for i in range(1, N + 1):
    if not N % i:
        divisors.append(i)
P = [i for i in range(N) if S[i] == 'P']
possible = set()
for d in divisors:
    mod = [1] * d
    for p in P:
        mod[p % d] = 0
    if sum(mod):
        possible.add(d)

ans = 0
for i in range(1, N):
    if gcd(i, N) in possible:
        ans += 1

print(ans)
