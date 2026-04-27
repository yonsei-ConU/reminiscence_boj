import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n, S = minput()
    t = list(minput())
    assert t == sorted(t)
    v = tuple(minput())
    heap = []
    s = 0
    ptr = 0
    ans = 0
    while ptr < n and t[ptr] < S:
        ans += (S - t[ptr]) * v[ptr]
        ptr += 1
    time = S
    while ptr < n:
        if not heap:
            ptr += 1
            continue
        while ptr < n and t[ptr] == time:
            s += v[ptr]
            heappush(heap, -v[ptr])
            ptr += 1
        s += heappop(heap)
        ans += s
        time += 1
    print(ans)
