import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, T = minput()
imos = [0] * 100002

for _ in range(N):
    for __ in range(int(input_())):
        S, E = minput()
        imos[S] += 1
        imos[E] -= 1

real = [0] * 100002
cur_sum = 0
for i in range(100002):
    cur_sum += imos[i]
    real[i] = cur_sum

ps = [0] * 100002
cur_sum = 0
for i in range(100002):
    cur_sum += real[i]
    ps[i] = cur_sum
# print(imos[:20])
# print(real[:20])
# print(ps[:20])
ans_time = T
ans_val = ps[T - 1]
for i in range(T + 1, 100002):
    tmp = ps[i] - ps[i - T]
    if tmp > ans_val:
        ans_time = i + 1
        ans_val = tmp

print(ans_time - T, ans_time)
# print(ans_val)
