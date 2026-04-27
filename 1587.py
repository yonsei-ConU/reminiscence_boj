import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


nA, nB = minput()
M = int(input_())
ans = nA // 2 + nB // 2
for i in range(M):
    a, b = minput()
    t = 1 + (a - 1) // 2 + (nA - a) // 2 + (b - 1) // 2 + (nB - b) // 2
    ans = max(ans, t)

print(ans)
