import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if N == 1: exit(print(0))  # 0만 살 수 있음
P = list(minput())
M = int(input_())

all_min = min(P)
posi_min = 999999999
posi_min_val = 0
for i in range(1, N):
    if P[i] <= posi_min:
        posi_min = P[i]
        posi_min_val = i

if posi_min > M: exit(print(0))  # 0만 살 수 있음
t = posi_min
length = 0
while t <= M:
    length += 1
    t += all_min

extra_money = M - t + all_min
if all_min != posi_min:
    res = [posi_min_val] + [0] * (length - 1)
else:
    res = [posi_min_val] * length
extra_cost_zero = [P[i] - all_min for i in range(N)]
extra_cost_nz = [P[i] - posi_min for i in range(N)]

for idx in range(length):
    if res[idx]:
        cost = extra_cost_nz
    else:
        cost = extra_cost_zero

    for num in range(res[idx] + 1, N)[::-1]:
        if cost[num] <= extra_money:
            res[idx] = num
            extra_money -= cost[num]
            break

for r in res: sys.stdout.write(str(r))
