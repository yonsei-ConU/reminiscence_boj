import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class mystr:
    def __init__(self, a):
        self.s = a

    def __lt__(self, other):
        if self.s.startswith(other.s):
            return True
        elif other.s.startswith(self.s):
            return False
        return self.s < other.s


N = int(input_())
heap = []
for _ in range(N):
    heappush(heap, mystr(input_().rstrip()))

ans = []
while heap:
    cur = heappop(heap).s
    if len(cur) > 1:
        heappush(heap, mystr(cur[1:]))
    ans.append(cur[0])

print(''.join(ans))
