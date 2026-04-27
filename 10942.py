import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
hj = list(minput())
pal = [[False] * (N - i) for i in range(N)]
# pal[i][j]: 길이가 i+1이고 j번째 글자부터인 문자열이 팰린드롬이다.
pal[0] = [True] * N
for j in range(N - 1):
    if hj[j] == hj[j + 1]:
        pal[1][j] = True

for i in range(2, N):
    for j in range(N - i):
        pal[i][j] = hj[j] == hj[j + i] and pal[i - 2][j + 1]

for _ in range(int(input_())):
    S, E = minput()
    print(+pal[E - S][S - 1])
