import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
R, G, B = minput()
if max(R, G, B) > N * M // 2: exit(print("NO"))

ans = [[''] * M for _ in range(N)]
cnt = 0
if R > G > B:
    s = 'R' * R + 'G' * G + 'B' * B
elif R > B > G:
    s = 'R' * R + 'B' * B + 'G' * G
elif G > R > B:
    s = 'G' * G + 'R' * R + 'B' * B
elif G > B > R:
    s = 'G' * G + 'B' * B + 'R' * R
elif B > R > G:
    s = 'B' * B + 'R' * R + 'G' * G
elif B > G > R:
    s = 'B' * B + 'G' * G + 'R' * R
elif R == G:
    if R > B:
        s = 'R' * R + 'B' * B + 'G' * G
    else:
        s = 'B' * B + 'R' * R + 'G' * G
elif G == B:
    if G > R:
        s = 'B' * B + 'R' * R + 'G' * G
    else:
        s = 'R' * R + 'G' * G + 'B' * B
elif R == B:
    if R > G:
        s = 'R' * R + 'G' * G + 'B' * B
    else:
        s = 'G' * G + 'B' * B + 'R' * R

for i in range(N):
    for j in range(i % 2, M, 2):
        ans[i][j] = s[cnt]
        cnt += 1

for i in range(N):
    for j in range((i + 1) % 2, M, 2):
        ans[i][j] = s[cnt]
        cnt += 1

assert cnt == N * M
print('YES')
for a in ans: print(''.join(a))
