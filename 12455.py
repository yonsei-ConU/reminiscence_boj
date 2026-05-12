import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    N, K = minput()
    coffees = []
    for i in range(N):
        c, t, s = minput()
        coffees.append((K - t, -s, c))
    coffees.sort(reverse=True)
    ans = 0
    heap = []
    for day in range(K):
        while coffees and coffees[-1][0] <= day:
            _, s, c = coffees.pop()
            heappush(heap, (s, c))
        if not heap: continue
        s, c = heappop(heap)
        ans -= s
        c -= 1
        if c:
            heappush(heap, (s, c))
    print(f"Case #{tc}: {ans}")
