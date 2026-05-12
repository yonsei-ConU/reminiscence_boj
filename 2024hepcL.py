import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
from heapq import heappush, heappop

N = int(input_())
heap = []
for _ in range(N):
    heappush(heap, list(minput())[::-1])
M = int(input_())
pending = []
for _ in range(M):
    pending.append(list(minput()))
pending.sort(reverse=True)
time = 0

while heap or pending:
    try:
        due, time_cost = heappop(heap)
    except IndexError:
        w, tc, d = pending.pop()
        heappush(heap, [d, tc])
        time = w
        continue
    if time + time_cost > due:
        print('NO')
        exit()
    elif pending and time_cost + time > pending[-1][0]:
        w, tc, d = pending.pop()
        heappush(heap, [d, tc])
        time_cost_left = time_cost - w + time
        heappush(heap, [due, time_cost_left])
        time = w
    else:
        time += time_cost

print('YES')
print(time)
