import sys
from collections import Counter
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, B = minput()
A = list(minput())
new_seq = []
for i in range(N):
    a = A[i]
    if a < B:
        new_seq.append(-1)
    elif a > B:
        new_seq.append(1)
    else:
        new_seq.append(0)
        idx = i

left = [0]
for i in range(idx - 1, -1, -1):
    left.append(left[-1] - new_seq[i])
left = left[1:]

right = [0]
for i in range(idx + 1, N):
    right.append(right[-1] + new_seq[i])
right = right[1:]

lc = Counter(left)
rc = Counter(right)
ans = lc[0] + rc[0] + 1
for x in lc:
    ans += lc[x] * rc[x]

print(ans)
