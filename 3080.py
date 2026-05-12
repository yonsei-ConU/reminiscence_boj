import sys
sys.setrecursionlimit(3080)
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dfs(start, end, depth):
    global ans
    if start == end: return
    # null
    lo = start - 1
    hi = end + 1
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if len(names[mid]) == depth:
            lo = mid
        else:
            hi = mid
    left = hi
    mult = hi - start
    for c in range(65, 65 + 26):
        d = chr(c)
        lo = left - 1
        hi = end + 1
        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            if names[mid][depth] == d:
                lo = mid
            else:
                hi = mid
        if lo > left - 1:
            dfs(left, lo, depth + 1)
            mult += 1
        left = hi
    ans = ans * fact[mult] % MOD


N = int(input_())
MOD = 10 ** 9 + 7
fact = [1, 1]
for i in range(2, 3001):
    fact.append(fact[i - 1] * i % MOD)
ans = 1
names = sorted([input_().rstrip() for _ in range(N)])
dfs(0, N - 1, 0)
print(ans)
