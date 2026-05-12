import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


grundy = [[0] * 3000 for _ in range(3000)]
for i in range(513):
    for j in range(513):
        if not i and not j: continue
        next_state = set()
        for x in range(i):
            next_state.add(grundy[x][j])
        for y in range(j):
            next_state.add(grundy[i][y])
        # next_state.add(grundy[i - 1][j - 1])
        mex = 0
        while mex in next_state:
            mex += 1
        grundy[i][j] = mex

for i in range(385):
    for j in range(385):
        print(f"{grundy[i][j]: >4}", end='')
    print()
print()
for i in range(33):
    for j in range(33):
        print(f"{grundy[i * 16][j * 16] // 16: >3}", end='')
    print()
print()
for i in range(3):
    for j in range(3):
        print(f"{grundy[i * 256][j * 256] // 256: >3}", end='')
    print()
