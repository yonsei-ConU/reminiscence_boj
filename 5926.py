import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ids = set()
cows = []
for _ in range(N):
    x, ID = minput()
    ids.add(ID)
    cows.append((x, ID))
cows.sort()
