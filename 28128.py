import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
if N == 1 and M == 1:
    exit(print("MANIPULATED"))
names = [input_().rstrip().split() for _ in range(N)]
ans = set()
# 가로 2,3 세로 1
for i in range(N):
    for j in range(M - 1):
        if names[i][j] == names[i][j + 1]:
            ans.add(names[i][j])
        elif j != M - 2 and names[i][j] == names[i][j + 2]:
            ans.add(names[i][j])

for i in range(N - 1):
    for j in range(M):
        if names[i][j] == names[i + 1][j]:
            ans.add(names[i][j])
        elif i != N - 2 and names[i][j] == names[i + 2][j]:
            ans.add(names[i][j])

ans = sorted(ans)
if not ans:
    print("MANIPULATED")
else:
    for value in ans:
        print(value)
