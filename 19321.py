import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
f = list(minput())
M = max(f)
cnt = [0] * n
for v in f:
    cnt[v - 1] += 1
num = [0] * n
cur = 1
for i in range(n):
    num[i] = cur
    cur += cnt[i]
for i in range(n - 1):
    num[i] = num[i + 1] - 1
num[n - 1] = n

ans = [0] * n
for i in range(n):
    ans[i] = num[f[i] - 1]
    num[f[i] - 1] -= 1

print(*ans)
    
