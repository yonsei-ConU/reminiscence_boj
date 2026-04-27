import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if N == 2: exit(print(-1))
magic = 500000
x = N * (N - 1) // 2
for t in range(N, 2 * N):
    if not (x + t) % N:
        break
else:
    assert False

r = list(range(1, N)) + [t]
ans = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        ans[i][j] = (r[i] + 1) + magic * (r[j] + 1)

for i in range(N):
    t1 = ans[i]
    if sum(t1) // N not in t1:
        print(1 / 0)
    t2 = [ans[j][i] for j in range(N)]
    if sum(t2) // N not in t2:
        print(1 / 0)

for a in ans: print(*a)
