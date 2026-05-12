import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


X, Y, Z = minput()
last = {(X, Y, Z): (X, Y, Z)}
q = deque()
q.append((X, Y, Z))
cnt = 0

try:
    while q:
        cnt += 1
        x, y, z = q.popleft()

        i = min(y, z)
        flag = False
        while i - min(y, z) < max(y, z):
            i <<= 1
            if i - min(y, z) == max(y, z):
                flag = True
                break
        if flag:
            break

        if x < y and (2 * x, y - x, z) not in last:
            last[(2 * x, y - x, z)] = (x, y, z)
            q.append((2 * x, y - x, z))

        elif x > y and (x - y, 2 * y, z) not in last:
            last[(x - y, 2 * y, z)] = (x, y, z)
            q.append((x - y, 2 * y, z))

        if x < z and (2 * x, y, z - x) not in last:
            last[(2 * x, y, z - x)] = (x, y, z)
            q.append((2 * x, y, z - x))

        elif x > z and (x - z, y, 2 * z) not in last:
            last[(x - z, y, 2 * z)] = (x, y, z)
            q.append((x - z, y, 2 * z))

except KeyboardInterrupt:
    exit(print(cnt))

ans = [(x, y, z)]
cur = (x, y, z)
while cur != (X, Y, Z):
    cur = last[cur]
    ans.append(cur[:])

ans.reverse()
print(cnt)
print(*ans, sep="""
""")
