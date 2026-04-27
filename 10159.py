import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
from collections import deque

N = int(input_())
M = int(input_())
weight_info = [([], []) for _ in range(N + 1)]

for _ in range(M):
    heavy, light = minput()
    weight_info[heavy][0].append(light)
    weight_info[light][1].append(heavy)

for i in range(1, N + 1):
    found = [False] * (N + 1)
    found[i] = True
    ans = N - 1
    for j in [0, 1]:
        q = deque([i])
        while q:
            now = q.popleft()
            for nxt in weight_info[now][j]:
                if not found[nxt]:
                    q.append(nxt)
                    found[nxt] = True
                    ans -= 1
    print(ans)
