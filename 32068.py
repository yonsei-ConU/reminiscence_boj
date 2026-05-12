import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    L, R, S = minput()
    l, r = L - S, R - S
    m = l
    if abs(l) >= abs(r):
        m = r
    if m == 0:
        print(1)
    elif m > 0:
        print(m * 2)
    else:
        print(-m * 2 + 1)
