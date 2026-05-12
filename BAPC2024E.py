import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
d = {}
if n == 3:
    exit(print("! 1 2 3"))

print("? 1", flush=True)
m = int(input_())
d[1] = m
print("?", n, flush=True)
M = int(input_())
d[n] = M
mM = (m + M) >> 1
lo = 0
hi = n - 1
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    if mid + 1 in d:
        val = d[mid + 1]
    else:
        print("?", mid + 1, flush=True)
        val = int(input_())
        d[mid + 1] = val
    if val >= mM:
        hi = mid
    else:
        lo = mid

if lo + 1 not in d:
    print('?', lo + 1, flush=True)
    d[lo + 1] = int(input_())
lo_v = abs(d[lo + 1] - mM)
if hi + 1 not in d:
    print('?', hi + 1, flush=True)
    d[hi + 1] = int(input_())
hi_v = abs(d[hi + 1] - mM)

if lo_v < hi_v:
    if lo:
        print("!", 1, lo + 1, n, flush=True)
    else:
        print("!", 1, hi + 1, n, flush=True)
else:
    if hi != n - 1:
        print("!", 1, hi + 1, n, flush=True)
    else:
        print("!", 1, lo + 1, n, flush=True)
