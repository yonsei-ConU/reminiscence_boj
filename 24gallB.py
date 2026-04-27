import sys
from collections import Counter
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, K = minput()
friends = [input_().rstrip() for _ in range(N)]

table = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        s1 = friends[i]
        s2 = friends[j]
        for x in range(M):
            if s1[x] != s2[x]:
                break
        else:
            x += 1
        table[i][j] = table[j][i] = x + 1

ans_val = 998999999
ans_str = ''
for i in range(N):
    t = Counter(table[i])
    remain = N
    for m in range(M + 1):
        if m in t:
            remain -= t[m]
        if remain <= K:
            if m < ans_val:
                ans_val = m
                ans_str = friends[i][:m]
            break

if ans_val >= 998999999:
    print(-1)
else:
    print(ans_val)
    trans = str.maketrans('RSP', 'SPR')
    print(ans_str.translate(trans))
