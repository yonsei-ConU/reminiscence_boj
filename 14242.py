import sys
from math import comb
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 10 ** 9 + 7
factorial = [1, 1]
for i in range(2, 16):factorial.append(factorial[-1] * i % MOD)

N = 3
if N == 2: exit(print(2))
ans = factorial[N - 1] // 2
for i in range(1, N):
    ans = (ans + factorial[i] * 2) % MOD
    print(ans)

print(ans)
