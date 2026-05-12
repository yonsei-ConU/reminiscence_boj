import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


w, n = minput()
A = tuple(minput())
pair_sum = {}

for i in range(n):
    for j in range(i + 1, n):
        pair_sum[A[i] + A[j]] = (i, j)

for i in range(n):
    for j in range(i + 1, n):
        if w - A[i] - A[j] not in pair_sum:
            continue
        p, q = pair_sum[w - A[i] - A[j]]
        if i != p and i != q and j != p and j != q:
            exit(print("YES"))

print("NO")
