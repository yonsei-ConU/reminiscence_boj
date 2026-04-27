import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
from heapq import heappop, heappush

N, M, K = minput()
importance = []
for i in range(N):
    im = int(input_())
    heappush(importance, (-im, im))

day = 0
satisfaction = 0
satisfaction_list = []
while True:
    im = heappop(importance)[1]
    if im <= K:
        break
    else:
        satisfaction = satisfaction // 2 + im
        satisfaction_list.append(satisfaction)
        im -= M
        heappush(importance, (-im, im))
        day += 1

print(day)
print(*satisfaction_list, sep='\n')
