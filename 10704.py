import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
t = 0
ans = []
m = 9999999999
cur = N - K + 1
while cur > 0:
    while cur <= N - K * t:
        ans.append(str(cur))
        m = min(m, cur)
        cur += 1
    t += 2
    cur = N - K * t + 1
    t -= 1

if m == 1:
    t -= 1

for i in range(1, m):
    ans.append(str(i))

if t + 1 > K:
    print(-1)
else:
    print(' '.join(ans))
