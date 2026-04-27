import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for n in range(1, int(input_()) + 1):
    grundy = [0] * 31
    for i in range(1, 31):
        next_state = set()
        for j in range(i - 1, max(-1, i - n - 1), -1):
            next_state.add(grundy[j])
        mex = 0
        while mex in next_state:
            mex += 1
        grundy[i] = mex
    if not grundy[30]:
        print(n)
