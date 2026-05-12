import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def discriminant(x):
    return B[x] - A[x] - (N - x - 1) * (U + D) <= 0


N, U, D = minput()
A = list(minput())
B = list(minput())
ans = 0
f = []
shift = 0

for i in range(N):
    if discriminant(i):
        ans += B[i] + shift
        shift -= D
    else:
        ans += A[i] + shift
        shift += U
    f.append(ans)

for val in f: print(val)
