import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, k = minput()
if not k: exit(print(-1))
ans = list(range(1, n + 1))
if not k % 2:
    ans[0] = n
    ans[-1] = 1
for i in range((k - 1) >> 1):
    idx = i * 2 + 1
    ans[idx], ans[idx + 1] = ans[idx + 1], ans[idx]

print(*ans)
