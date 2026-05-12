import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, T = minput()
rock = {(0, 0): 0}
for i in range(n):
    x, y = minput()
    rock[(x, y)] = 0

q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if not dx and not dy: continue
            nx, ny = x + dx, y + dy
            if (nx, ny) in rock and not rock[(nx, ny)]:
                rock[(nx, ny)] = rock[(x, y)] + 1
                q.append((nx, ny))
                if ny == T:
                    exit(print(rock[(nx, ny)]))

print(-1)
