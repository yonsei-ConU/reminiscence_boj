# 9m 47.11s

import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
cost_per_weight = [int(input_()) for _ in range(N)]  # 무게당 가격 0인덱스
weights = [int(input_()) for _ in range(M)]  # 차 무게들 0인덱스
waiting = deque()  # 기다리고 있는 차번호 1인덱스
empty = set(range(1, N + 1))  # 비어 있는 주차공간 1인덱스
parking = [0] * (N + 1)  # 주차공간마다 있는 차 없으면 0, 1인덱스
ans = 0

for i in range(2 * M):
    log = int(input_())
    if log > 0:
        if not empty:
            waiting.append(log)
        else:
            x = min(empty)
            empty.remove(x)
            parking[x] = log
    else:
        log *= -1
        x = parking.index(log)
        ans += weights[log - 1] * cost_per_weight[x - 1]
        empty.add(x)
        if waiting:
            nxt = waiting.popleft()
            x = min(empty)
            empty.remove(x)
            parking[x] = nxt

print(ans)
