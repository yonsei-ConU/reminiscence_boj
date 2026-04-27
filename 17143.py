import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


R, C, M = minput()
if not M: exit(print(0))
shark = [[[] for _ in range(C)] for __ in range(R)]
for _ in range(M):
    r, c, s, d, z = minput()
    shark[r][c] = [s, d, z, 0]
    # s is speed
    # d is direction
    # d=1 then up, d=2 then down, d=3 then right, d=4 then left.
    # z is size

ans = 0

for i in range(C):
    # nakksiwang move
    for j in range(R):
        if shark[j][i]:
            ans += shark[j][i][2]
            shark[j][i] = []
    # sharks move
    for p in range(R):
        for q in range(C):
