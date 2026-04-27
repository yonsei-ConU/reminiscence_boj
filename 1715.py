import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
from heapq import heapify, heappush, heappop

heap = [int(input_()) for _ in range(int(input_()))]
heapify(heap)
ans = 0
while len(heap) > 1:
    a, b = heappop(heap), heappop(heap)
    c = a + b
    heappush(heap, c)
    ans += c

print(ans)
