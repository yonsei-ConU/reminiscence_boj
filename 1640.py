import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
row = [0] * N
col = [0] * M
for i in range(N):
    S = input_().rstrip()
    for j in range(M):
        s = S[j]
        if s == '0':
            row[i] ^= 1
            col[j] ^= 1

r = sum(row)
c = sum(col)
ans = 999999
if r & 1:
    if c & 1:
        ans = min(ans, r + c, N + M - r - c)
else:
    if (M - c) & 1:
        ans = min(ans, r + M - c, c + N - r)

print(ans if ans != 999999 else -1)
