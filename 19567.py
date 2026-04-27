import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
frogs = []
minX = -10 ** 10
maxX = 10 ** 10
t = [False, False]

for _ in range(N):
    x, y, c = minput()
    minX = max(minX, x - c)
    maxX = min(maxX, x + c)
    frogs.append([x, y, c])
    t[(x + y + c) & 1] = True

if minX > maxX or sum(t) != 1:
    exit(print("NO"))

lo = minX - 1
hi = maxX + 1
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    minY = -10 ** 10
    maxY = 10 ** 10
    for x, y, c in frogs:
        c_left = c - abs(x - mid)
        minY = max(minY, y - c_left)
        maxY = min(maxY, y + c_left)
    if minY > maxY:
        
