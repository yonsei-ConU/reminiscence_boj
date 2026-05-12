import sys
from heapq import heappush, heappop
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
univ = []
max_day = 0

for i in range(n):
    p, d = minput()
    univ.append((d, -p))
    max_day = max(max_day, d)

univ = sorted(univ)
heap = []
ans = 0

for cur_day in range(1, max_day + 1)[::-1]:
    while univ and univ[-1][0] >= cur_day:
        heappush(heap, univ[-1][1])
        univ.pop()
    if heap:
        ans -= heappop(heap)

print(ans)

# 마지막 강연의 기한을 편의상 M으로 가정한다.
# 시간이 역순으로 간다고 가정한다. -> "언제까지만 할 수 있는" 강연이 아니라 "언제부터 할 수 있는 강연"으로 바뀐다.
# 지금 시각이 t일 때, 돈을 최대로 벌 수 있는 강연의 집합 OPT를 상정하자.
# 우선 t = M일 때 우리는 "t = M부터 할 수 있는 강연들 중 가장 비싼 것"을 골랐기 때문에 이것은 OPT에 비해서 나쁘지 않다.
# 모든 날에 대해서 SOL은 "강연을 할 수 있는데도 강연을 하지 않는 경우"가 존재하지 않도록 고르게 된다.
# 각각의 날에 대해서 고를 수 있는 강연의 개수는 {0} 또는 {0, 1}로 표현되며, {0, 1}인 경우 SOL은 무조건 1을 선택한다.
# t = x일 때 OPT는 a개, SOL은 b개의 강연을 했다고 하고, a <= b라고 가정한다.
# t = x - 1일 때 고를 수 있는 강연의 개수가 {0}이면 t = x - 1일 때 OPT와 SOL은 각각 a, b개의 강연을 진행한 상태이고, a <= b가 유지된다.
# t = x - 1일 때 고를 수 있는 강연의 개수가 {0, 1}이면
# OPT는 a개 또는 a + 1개의 강연을 고른 상태, SOL은 b + 1개의 강연을 고른 상태이며, a <= b가 유지된다.
# ==> SOL은 OPT에 비해 모든 시각에서 더 많은 개수의 강연을 고른다는 것이 증명됨.
