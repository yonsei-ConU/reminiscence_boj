import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
planks = sorted([int(input_()) for _ in range(N)])
heap = [planks[0]]
ans = 0

for val in planks[1:]:
    ...
