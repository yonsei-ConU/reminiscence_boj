import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def simulate(start_idx, v):
    for idx in range(start_idx + 1, N):
        v += A[idx]
        if v > x:
            v = x
        elif v < 0:
            v = 0
    return v


x, N = minput()
A = list(minput())
M = m = 0
Midx = midx = 0
psum = 0

for idx in range(N):
    psum += A[idx]
    if psum >= M:
        M = psum
        Midx = idx
    if psum <= m:
        m = psum
        midx = idx

small = simulate(midx, 0)
large = simulate(Midx, x)

for _ in range(int(input_())):
    y = int(input_())
    if -m <= y <= x - M:
        print(y + psum)
    elif y < -m:
        print(small)
    else:
        print(large)
