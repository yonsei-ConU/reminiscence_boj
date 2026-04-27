import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
buildings = sorted([list(minput()) for _ in range(N)], key=lambda x: (x[0], -x[1], x[2]))
heap = [(0, 9999999999)]
ans = []
cur_height = 0

for L, H, R in buildings:
    while heap and heap[0][1] < L:
        h, r = heappop(heap)
        if -h == cur_height and not (heap[0][1] >= L and -heap[0][0] == cur_height):
            ans.append(str(r))
            while heap and heap[0][1] <= L:
                heappop(heap)
            ans.append(str(-heap[0][0]))
            cur_height = -heap[0][0]
    heappush(heap, (-H, R))
    if -heap[0][0] > cur_height:
        ans.append(str(L))
        ans.append(str(H))
        cur_height = -heap[0][0]

while len(heap) > 1:
    h, r = heappop(heap)
    if -h == cur_height and not (heap[0][1] >= r and -heap[0][0] == cur_height):
        ans.append(str(r))
        while len(heap) > 1 and heap[0][1] <= r:
            heappop(heap)
        ans.append(str(-heap[0][0]))
        cur_height = -heap[0][0]

print(' '.join(ans))
