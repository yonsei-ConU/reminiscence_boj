import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
val = [int(input_()) for _ in range(N)]
ps = [0]
cur_sum = 0
for i in range(N):
    cur_sum += val[i]
    ps.append(cur_sum)

ps_min = []
cur_min = 10 ** 18
for i in range(N + 1):
    if ps[i] < cur_min:
        ps_min.append(i)
        cur_min = ps[i]
    else:
        ps_min.append(ps_min[-1])

ans = 0
for i in range(M - 1, N):
    ans = max(ans, ps[i + 1] - ps[ps_min[i - M + 1]])

print(ans)
