import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class Time:
    def __init__(self, t):
        if isinstance(t, str):
            self.h, self.m = map(int, t.split(':'))
            if self.h == 12:
                self.h = 0
        else:
            dh, self.m = divmod(t[1], 60)
            self.h = (t[0] + dh) % 12

    def __add__(self, rhs):
        ret = Time((self.h, self.m))
        ret.m += rhs.m
        while ret.m >= 60:
            ret.m -= 60
            ret.h += 1
        ret.h += rhs.h
        while ret.h >= 12:
            ret.h -= 12
        return ret

    def __sub__(self, rhs):
        ret = Time((self.h, self.m))
        ret.m -= rhs.m
        while ret.m < 0:
            ret.m += 60
            ret.h -= 1
        ret.h -= rhs.h
        while ret.h < 0:
            ret.h += 12
        return ret

    def __eq__(self, rhs):
        return self.h == rhs.h and self.m == rhs.m

    def __hash__(self):
        return hash((self.h, self.m))

    def __repr__(self):
        return f"{self.h}:{self.m}"


M = int(input_())
records = [Time(input_()) for _ in range(M)]
ans = M
for R in range(1, 721):
    clocks = set()
    for i in range(M):
        clocks.add(records[i] - Time((i // 60 * R, i % 60 * R)))
    ans = min(ans, len(clocks))

print(ans)
