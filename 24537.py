import sys
from math import gcd
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
cnt = [0] * 1000001
for v in list(minput()):
    cnt[v] += 1

memo = [-1] * 1000001
for _ in range(int(input_())):
    q = int(input_())
    if memo[q] == -1:
        ans = 0
        g = -1
        for i in range(q, 1000001, q):
            ans += cnt[i]
            if cnt[i]:
                if g == -1:
                    g = i
                else:
                    g = gcd(g, i)
        if g == q:
            memo[q] = ans
        else:
            memo[q] = 0
    print(memo[q] if memo[q] else -1)
