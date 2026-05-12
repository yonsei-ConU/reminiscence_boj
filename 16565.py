import sys
from math import comb
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 10007
N = int(input_())
ans = 0
sign = 1
for i in range(4, 53, 4):
    if N < i:
        break
    ans = (ans + sign * comb(13, i >> 2) * comb(52 - i, N - i)) % MOD
    sign *= -1

print(ans)
