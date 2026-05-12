import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())

start = []
for i in range(min(N, 3)):
    x = int(input_())
    start.append(x)
    start.sort()
    print(start[i >> 1])
if N < 3:
    exit()
max_heap = [(-start[0], start[0])]
min_heap = [(start[2], start[2])]
root = start[1]

for i in range(3, N):
    x = int(input_())
    _, v1 = heappop(max_heap)
    _, v2 = heappop(min_heap)
    t = sorted([v1, v2, x, root])
    if i & 1:
        a = t.pop()
        heappush(min_heap, (a, a))
        a = t.pop()
        heappush(min_heap, (a, a))
        root = t.pop()
        a = t.pop()
        heappush(max_heap, (-a, a))
    else:
        a = t.pop()
        heappush(min_heap, (a, a))
        root = t.pop()
        a = t.pop()
        heappush(max_heap, (-a, a))
        a = t.pop()
        heappush(max_heap, (-a, a))
    print(root)
