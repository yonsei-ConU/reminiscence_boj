import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


T = int(input_())
n = int(input_())
A = list(minput())
m = int(input_())
B = list(minput())

A_ps = [0]
A_sum = 0
for i in range(n):
    A_sum += A[i]
    A_ps.append(A_sum)

B_ps = [0]
B_sum = 0
for i in range(m):
    B_sum += B[i]
    B_ps.append(B_sum)

left = []
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        left.append(A_ps[j] - A_ps[i])

right = []
for i in range(m + 1):
    for j in range(i + 1, m + 1):
        right.append(B_ps[j] - B_ps[i])
right.sort()
ans = 0

for i in range(len(left)):
    lo = -1
    hi = len(right)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if left[i] + right[mid] >= T:
            hi = mid
        else:
            lo = mid
    min_idx = hi
    lo = -1
    hi = len(right)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if left[i] + right[mid] > T:
            hi = mid
        else:
            lo = mid
    max_idx = lo
    ans += max_idx - min_idx + 1

print(ans)
