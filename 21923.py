import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
scores = [list(minput()) for _ in range(N)]
# dp[i][j][k] = ((i, j) 칸, k는 방향 바꿨는지 안바꿨는지
dp = [[[-100000000, -100000000] for _ in range(M)] for __ in range(N)]

