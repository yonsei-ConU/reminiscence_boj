import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def arrive_time(t):
    for i in range(N):
        t += E[i]
        A, B, C, D = traffic[i]
        X = (t - C) // A
        if t < C: t = C + D
        elif C + A * X <= t and t + D <= C + A * X + B: t += D
        else: t = A * (X + 1) + C + D
        if t > T: break
    t += E[N]
    return t


for _ in range(int(input_())):
    N, T = minput()
    traffic = [list(minput()) for _ in range(N)]
    E = list(minput())
    lo = -1
    hi = T + 1
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        t = arrive_time(mid)
        if t > T:
            hi = mid
        else:
            lo = mid
    ans = 1
    if lo != -1 and arrive_time(lo) == T:
        ans = 0
    if arrive_time(hi) == T:
        ans = 0
    print('YNEOS'[ans::2])
