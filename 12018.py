import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, m = minput()
subjects = []

for _ in range(n):
    P, L = minput()
    M = sorted(list(minput()), reverse=True)
    if P < L:
        subjects.append(1)
    else:
        subjects.append(M[L - 1])

ans = 0
subjects.sort(reverse=True)
while m >= 0 and subjects:
    if subjects[-1] <= m:
        m -= subjects.pop()
        ans += 1
    else:
        break

print(ans)
