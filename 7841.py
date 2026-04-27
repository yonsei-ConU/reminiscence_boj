import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
points = [tuple(minput()) for _ in range(N)]
pset = set(tuple(points))
ans = 0
for i in range(N):
    for j in range(i):
        x, y = points[i]
        a = points[j][0] - points[i][0]
        b = points[j][1] - points[i][1]
        if (((x + b, y - a) in pset and (x + a + b, y + b - a) in pset) or
            ((x - b, y + a) in pset and (x + a - b, y + a + b) in pset)):
            ans += 1
print(ans)
