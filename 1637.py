import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def get_cnt(x):
    ret = 0
    for A, C, B in mTE:
        ret += max(0, (min(x, C) - A) // B + 1)
    return ret


N = int(input_())
mTE = [tuple(minput()) for _ in range(N)]
lo = 0
hi = 2147483648
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    if get_cnt(mid) & 1:
        hi = mid
    else:
        lo = mid

if hi == 2147483648:
    print("NOTHING")
else:
    print(hi, get_cnt(hi) - get_cnt(lo))
