import sys
from math import isqrt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


M = int(input_())
N = int(input_())
K = int(input_())
# 중심 (x, y), 가중치 B, 반지름 R -> (y, x, R, B)
shops = []
for i in range(K):
    y, x, R, B = minput()
    shops.append((y - 1, x - 1, R, B))

ans_B = 0
ans_points = 0
for i in range(N):
    imos = [0] * M
    for y, x, R, B in shops:
        D = R ** 2 - (i - y) ** 2
        if D < 0:
            continue
        lower = x - isqrt(D)
        upper = x + isqrt(D)
        if lower < M:
            imos[max(0, lower)] += B
        if upper + 1 < M:
            imos[max(0, upper + 1)] -= B
    cur_sum = 0
    for j in range(M):
        cur_sum += imos[j]
        if cur_sum > ans_B:
            ans_B = cur_sum
            ans_points = 1
        elif cur_sum == ans_B:
            ans_points += 1

print(ans_B)
print(ans_points)
