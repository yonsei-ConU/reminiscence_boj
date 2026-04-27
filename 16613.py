import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


S = input_().rstrip()
even = S[::2]
odd = S[1::2]

lo = 0
hi = len(even) + 1
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    if even[:mid] in S:
        lo = mid
    else:
        hi = mid
even = lo
lo = 0
hi = len(odd) + 1
while lo + 1 < hi:
    mid = (lo + hi) >> 1
    if odd[:mid] in S:
        lo = mid
    else:
        hi = mid
odd = lo
print(min(max(even << 1, (odd << 1) | 1), len(S)))
