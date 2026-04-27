import sys
from heapq import heappop, heappush
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans = 0
cows = []
for i in range(N):
    a, t = minput()
    cows.append([a, t, i])

cows.sort(reverse=True)
heap = []
time = 0
while cows or heap:
    if not heap:
        time = max(time, cows[-1][0])
    while cows and cows[-1][0] <= time:
        a, t, i = cows.pop()
        heappush(heap, [i, t, a])
    _, t, a = heappop(heap)
    ans = max(ans, time - a)
    time += t

print(ans)
