import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
points = []
pset = set()
unavailable = set()
for i in range(N):
    s = input_().rstrip()
    for j in range(N):
        if s[j] == 'J':
            points.append((i, j))
            pset.add((i, j))
        elif s[j] == 'B':
            unavailable.add((i, j))

ans = 0
for i in range(len(points)):
    for j in range(i):
        x, y = points[i]
        a = points[j][0] - points[i][0]
        b = points[j][1] - points[i][1]
        chk = False
        if 0 <= x + b < N and 0 <= y - a < N and 0 <= x + a + b < N and 0 <= y + b - a < N:
            if ((x + b, y - a) in pset and (x + a + b, y + b - a) not in unavailable) or ((x + b, y - a) not in unavailable and (x + a + b, y + b - a) in pset):
                chk = True
        elif 0 <= x - b < N and 0 <= y + a < N and 0 <= x + a - b < N and 0 <= y + a + b < N:
            if ((x - b, y + a) in pset and (x + a - b, y + a + b) not in unavailable) or ((x - b, y + a) not in unavailable and (x + a - b, y + a + b) in pset):
                chk = True
        if chk:
            ans = max(ans, a * a + b * b)

print(ans)
