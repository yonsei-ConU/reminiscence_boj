import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()

X = []
Y = []
ans = 0

for _ in range(N):
    p, q = minput()
    X.append(p)
    Y.append(q)
    ans += abs(p) + abs(q)

X.sort()
Y.sort()

query = input_().rstrip()
x = 0
y = 0

for q in query:
    if q == 'S':
        lo = -1
        hi = N
        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            if Y[mid] > y:
                hi = mid
            else:
                lo = mid
        ans = ans + 2 * hi - N
        y += 1
    elif q == 'J':
        lo = -1
        hi = N
        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            if Y[mid] >= y:
                hi = mid
            else:
                lo = mid
        ans = ans + N - 2 * hi
        y -= 1
    elif q == 'I':
        lo = -1
        hi = N
        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            if X[mid] > x:
                hi = mid
            else:
                lo = mid
        ans = ans + 2 * hi - N
        x += 1
    elif q == 'Z':
        lo = -1
        hi = N
        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            if X[mid] >= x:
                hi = mid
            else:
                lo = mid
        ans = ans + N - 2 * hi
        x -= 1
    else: assert 0
    print(ans)
