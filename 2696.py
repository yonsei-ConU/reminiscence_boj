import sys
sys.stdin = open('data.txt')
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    M = int(input_())
    seq = []
    for __ in range((M + 9) // 10):
        seq.extend(list(minput()))
    print((M + 1) >> 1)
    start = []
    for i in range(min(M, 3)):
        x = seq[i]
        start.append(x)
        start.sort()
        if not i & 1:
            print(start[i >> 1], end=' ')
    if M < 3:
        continue
    max_heap = [(-start[0], start[0])]
    min_heap = [(start[2], start[2])]
    root = start[1]

    for i in range(3, M):
        x = seq[i]
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
        if not i & 1:
            if i % 20 == 18:
                print(root)
            else:
                print(root, end=' ')
    print()
