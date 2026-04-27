import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def f(i):
    goal = i + 1
    pos, idx = ud[i]
    for j in range(pos - goal):
        ans.append(f"{idx} U")
    for j in range(goal - pos):
        ans.append(f"{idx} D")
    ud[i] = (goal, idx)


N = int(input_())
ud = []
lr = []
for i in range(1, N + 1):
    R, C = minput()
    ud.append((R, i))
    lr.append((C, i))

ud.sort()
lr.sort()
ans = []
up = []
down = []
for i in range(N):
    goal = i + 1
    pos, idx = ud[i]
    if goal - pos < 0:
        up.append(i)
    elif goal - pos > 0:
        down.append(i)

up.sort(key=lambda i: ud[i][0])
down.sort(key=lambda i: ud[i][0], reverse=True)
for i in up:
    f(i)
for i in down:
    f(i)

for i in range(N):
    goal = i + 1
    pos, idx = lr[i]
    for j in range(pos - goal):
        ans.append(f"{idx} L")
    for j in range(goal - pos):
        ans.append(f"{idx} R")

print(len(ans))
print('\n'.join(ans))
