import sys
from heapq import heappop, heappush
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
l = list(minput())
appear = [[] for _ in range(K)]
for i in range(K):
    appear[l[i] - 1].append(i)

heap = []
for i in range(K):
    appear[i] = appear[i][1:][::-1]

ans = 0
in_tab = [False] * K + [False]
cnt = 0
for i in range(K):
    a = l[i] - 1
    if cnt < N:
        if not in_tab[a]:
            cnt += 1
            in_tab[a] = True
    elif not in_tab[a]:
        ans += 1
        in_tab[a] = True
        remove = K
        z = 1
        while not in_tab[remove] and z >= -i:
            z, remove = heappop(heap)
        in_tab[remove] = False
    if appear[a]:
        heappush(heap, (-appear[a].pop(), a))
    else:
        heappush(heap, (-998244353, a))

print(ans)
