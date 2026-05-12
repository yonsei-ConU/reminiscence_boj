import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, T = minput()
cows = [-1] * T
for _ in range(N):
    start, end = minput()
    start -= 1
    end -= 1
    cows[start] = max(cows[start], end)

last = -1
cur = -1
ans = 0
while 1:
    nxt = max(cows[last + 1:cur + 2])
    if nxt == -1:
        ans = -1
        break
    else:
        ans += 1
        last = cur
        cur = nxt
        if cur >= T - 1:
            break

print(ans)
