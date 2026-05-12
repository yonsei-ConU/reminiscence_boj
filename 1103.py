import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, M = minput()
board = [input_().rstrip() for _ in range(N)]
dp = [[[0] * M for _ in range(N)] for _ in range(N * M + 10)]
ans = 0
dp[0][0][0] = 1

for i in range(N * M + 9):
    for y in range(N):
        for x in range(M):
            mul = board[y][x]
            if mul == 'H' or not dp[i][y][x]:
                continue
            else:
                mul = int(mul)
            for j in range(4):
                ny, nx = y + dy[j] * mul, x + dx[j] * mul
                if 0 <= ny < N and 0 <= nx < M:
                    dp[i + 1][ny][nx] = 1
                    if board[ny][nx] != 'H':
                        ans = max(ans, i + 1)
                    else:
                        ans = max(ans, i)

if ans >= N * M + 5:
    print(-1)
else:
    print(ans + 1)


'''
counterexample (TLE)
5 7
1999996
3991999
9992999
9999999
9993994
'''

"""
### sol by JYJin

dp[cnt][y][x] = (y, x)에서 시작해서 cnt번만에 이동할 수 있는가? (bool)
구멍이 아닌 (y, x)에 대하여, dp[0][x][y] = 1 (base case)
for each (y, x), let board[y][x] = k
dp[cnt][ny][nx] == 1인 ny, nx가 존재한다면, dp[cnt + 1][y][x] = 1
무한 번 이동 가능한지 확인 -> 그냥 N*M번 돌려봐서 그때도 가능하다면 그냥 비둘기집 원리를 써서 무한 번이 가능하다...
무한 번이 안 된다면 dp[cnt]에 1이 존재하는 가장 큰 cnt가 답이겠죠.
"""
