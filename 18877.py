import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
intervals = sorted([list(minput()) for _ in range(M)])
lo = 0
hi = 10 ** 18 + 1
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    cnt = 1
    cur = intervals[0][0]
    while True:
        lo2 = -1
        hi2 = M
        nxt = -1
        while lo2 + 1 < hi2:
            mid2 = (lo2 + hi2) >> 1
            if intervals[mid2][0] <= cur + mid <= intervals[mid2][1]:
                nxt = cur + mid
                break
            elif cur + mid < intervals[mid2][0]:
                hi2 = mid2
            else:
                lo2 = mid2
        if nxt == -1:
            if hi2 == M:
                if cnt >= N:
                    lo = mid
                else:
                    hi = mid
                break
            nxt = intervals[hi2][0]
        cur = nxt
        cnt += 1
print(lo)
