import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
A_rev = [-1] * N
for i in range(N):
    A_rev[A[i] - 1] = i

ans = 0
cur = 0
last = -1
for i in range(N):
    if A_rev[i] > last:
        cur += 1
    else:
        ans = max(ans, cur)
        cur = 1
    last = A_rev[i]

ans = max(ans, cur)
print(N - ans)
