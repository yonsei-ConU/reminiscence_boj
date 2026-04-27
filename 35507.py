import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def ReLU(x):
    return max(x, 0)


for _ in range(int(input_())):
    N = int(input_())
    problems = [list(minput()) for _ in range(N)]
    a = b = c = d = 0
    ok = True
    for ra, rb, rc, p in problems:
        stat_delta = p - d
        req = ReLU(ra - a) + ReLU(rb - b) + ReLU(rc - c) + 1
        if req > stat_delta:
            ok = False
            break
        a = max(a, ra)
        b = max(b, rb)
        c = max(c, rc)
        d += req
    print("YNEOS"[1 - ok::2])
