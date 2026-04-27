import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


H, N = minput()
light = []
for i in range(N):
    r, c = minput()
    light.append((-c, i))

ans = [0] * N
cur = N
light.sort()
for _, idx in light:
    ans[idx] = cur
    cur -= 1

print("YES")
print(*ans)
