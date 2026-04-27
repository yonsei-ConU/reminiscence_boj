import sys
input_= sys.stdin.readline
def minput(): return map(int, input_().split())


N, S = minput()
arr = list(minput())
if N == 1:
    print(+(S == arr[0]))
    sys.exit(0)
left = []
right = []
for i in range(2 ** (N//2)):
    t = 0
    for j in range(N//2):
        if i & (1 << j):
            t += arr[j]
    left.append(t)

for i in range(2 ** (N - N//2)):
    t = 0
    for j in range(N - N//2):
        if i & (1 << j):
            t += arr[j + N//2]
    right.append(t)

left.sort()
right.sort()
# print(left, right)
ans = 0

for i in range(len(left)):
    lo = -1
    hi = len(right)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if left[i] + right[mid] >= S:
            hi = mid
        else:
            lo = mid
    min_idx = hi
    lo = -1
    hi = len(right)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if left[i] + right[mid] > S:
            hi = mid
        else:
            lo = mid
    max_idx = lo
    # print(max_idx, min_idx)
    ans += max_idx - min_idx + 1

if not S: ans -= 1
print(ans)
