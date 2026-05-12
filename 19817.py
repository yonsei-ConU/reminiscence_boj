# 3m 29.31s

import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
companies = []
real_max = 0
for _ in range(n):
    m, *s = minput()
    companies.append((m, max(s)))
    real_max = max(real_max, max(s))

ans = 0
for m, s in companies:
    ans += m * (real_max - s)

print(ans)
