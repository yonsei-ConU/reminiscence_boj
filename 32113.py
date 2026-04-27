import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
R, C = minput()
goal = [input_().rstrip() for _ in range(N)]
R -= 1; C -= 1
ans = []
for i in range(C):
    ans.append(f"L {R + 1} push")
for i in range(N - C - 1):
    ans.append(f"R {R + 1} push")
for i in range(R):
    ans.append("U 1 push")
for i in range(N - R - 1):
    ans.append("D 1 push")

for y in range(R - 1, -1, -1):
    for _ in range(N - 1):
        ans.append(f"R {y + 1} push")
    for x in range(1, N):
        if goal[y][x] == '.':
            ans.append(f"U {x + 1} pull")

for y in range(R, N):
    if y != R:
        for _ in range(N - 1):
            ans.append(f"R {y + 1} push")
    for x in range(1, N):
        if goal[y][x] == '.':
            ans.append(f"D {x + 1} pull")

for y in range(N):
    if goal[y][0] == '.':
        ans.append(f"L {y + 1} pull")

print(len(ans))
for s in ans:
    print(s)
