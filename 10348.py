import sys
from decimal import *
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
getcontext().prec = 150
pi = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
factorial_inv = [Decimal(1)] * 2
tmp = Decimal(1)
for i in range(2, 51):
    tmp /= Decimal(i)
    factorial_inv.append(tmp)


def twopi_mod(x):
    while x < -pi:
        x += 2*pi
    while x > 2*pi:
        x -= 2*pi
    return x


def sin(x):
    x = twopi_mod(x)
    r = Decimal(0)
    sgn_tmp = Decimal(1)
    for power in range(1, 51, 2):
        r += sgn_tmp * (x ** Decimal(power)) * factorial_inv[power]
        sgn_tmp *= -1
    return r


while 1:
    tc = tuple(minput())
    if tc == (0,):
        break
    W, N, D, *div = tc
    chk = [False] * (N + 1)
    for d in div:
        for x in range(d, N + 1, d):
            chk[x] = True
    shrine = [i for i in range(N + 1) if chk[i]]
    dist = [2000 * sin(pi / Decimal(N) * Decimal(shrine[i + 1] - shrine[i])) for i in range(len(shrine) - 1)]
    dist.append(2000 * sin(pi / Decimal(N) * Decimal(shrine[0] + N - shrine[-1])))
    # 최대 거리가 2000 + mid일 때 필요한 일꾼 수가 W 이하?
    dist = deque(dist)
    for i in range(len(dist)):
        lo = Decimal(0)
        hi = 2000 * pi
        while lo + Decimal('0.00000000000000000001') < hi:
            mid = (lo + hi) / 2
            cur_dist = Decimal(0)
            cur_worker_count = 1
            for j in range(len(dist) - 1):
                d = dist[j]
                if d + cur_dist > mid:
                    cur_dist = 0
                    cur_worker_count += 1
                else:
                    cur_dist += d
            if cur_worker_count <= W:
                hi = mid
            else:
                lo = mid
        ans = mid.quantize(Decimal('0.1'))
        if ans == Decimal('2987.7'):
            print(*(int(k) for k in dist), sep=', ')
        # print(ans + 2000)
        dist.rotate(1)
        # print(mid + 2000)
