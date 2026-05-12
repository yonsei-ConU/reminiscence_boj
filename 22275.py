import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, X = minput()
impossible = [0] * 200001
for i in range(N):
    start, duration = minput()
    for t in range(start, start + duration + 1):
        impossible[t] = 1

ans_time = 0
ans_conflict = 912768479637
for time in range(481):
    cur_conflict = 0
    cur_time = time
    while cur_time <= 200000:
        cur_conflict += impossible[cur_time]
        cur_time += X
    if cur_conflict < ans_conflict:
        ans_time = time
        ans_conflict = cur_conflict

print(ans_time, ans_conflict)
