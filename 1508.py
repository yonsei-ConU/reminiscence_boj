import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def f(mid):
    cur = 0
    ret = ['1']
    cnt = 1
    for i in range(1, K):
        cur += judge[i] - judge[i - 1]
        if cur > mid and cnt < M:
            ret.append('1')
            cur = 0
            cnt += 1
        else:
            ret.append('0')
    if cnt == M:
        return ret
    else:
        return False


N, M, K = minput()
judge = list(minput())
lo = 0
hi = N + 1
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    if not f(mid):
        hi = mid
    else:
        lo = mid

print(''.join(f(lo)))
