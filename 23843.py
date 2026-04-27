import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
t = sorted(list(minput()))
charge = [0] * M

while t:
    dt = t.pop()
    x = heappop(charge)
    heappush(charge, x + dt)

print(max(charge))
