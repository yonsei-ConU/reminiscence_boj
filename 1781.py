import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
problems = [list(minput()) for _ in range(N)]
heap = []
problems.sort()

ans = 0
t = 2 ** 31
while problems or (t and heap):
    while problems and t <= problems[-1][0]:
        _, cr = problems.pop()
        heappush(heap, -cr)
    if not heap:
        t = problems[-1][0] + 1
    else:
        ans -= heappop(heap)
    t -= 1

print(ans)
