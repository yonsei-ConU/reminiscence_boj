import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
one = []
for i in range(N):
    if A[i] == 1:
        one.append(i)

ans = min(one[-1] + 1, N - one[0])
for i in range(len(one)):
    idx = one[i]
    prev = one[i - 1] + 1 if i else 0
    nxt = one[i + 1] if i + 1 != len(one) else 0
    # < >=
    ans = min(ans, 2 * prev + N - idx)
    # <= >
    ans = min(ans, N + idx + 1 - (one[i + 1] if i + 1 != len(one) else 0))
    # > <=

print(ans)
