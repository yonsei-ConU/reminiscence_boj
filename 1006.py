import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
INF = 2000000000


def fill_table(dp):
    N = len(dp)
    for i in range(1, N):
        dp[i][3] = min(dp[i - 1]) + 2
        
        if A[i][0] + A[i - 1][0] <= W:
            dp[i][1] = min(dp[i - 1][3], dp[i - 1][2]) + 1
        
        if A[i][1] + A[i - 1][1] <= W:
            dp[i][2] = min(dp[i - 1][3], dp[i - 1][1]) + 1
        
        dp[i][0] = INF
        if A[i][0] + A[i][1] <= W:
            dp[i][0] = min(dp[i - 1]) + 1
        
        if A[i][0] + A[i - 1][0] <= W and A[i][1] + A[i - 1][1] <= W:
            dp[i][0] = min(dp[i][0], dp[i - 1][3])
    
    return dp


for _ in range(int(input_())):
    N, W = minput()
    A = [tuple(minput()) for _ in range(2)]
    A = list(zip(A[0], A[1]))

    ans = INF
    dp = [[INF, INF, INF, INF] for _ in range(N)]
    dp[0][3] = 2
    dp = fill_table(dp)
    ans = min(ans, min(dp[-1]))

    if A[0][0] + A[0][1] <= W:
        dp = [[INF, INF, INF, INF] for _ in range(N)]
        dp[0][0] = 1
        dp = fill_table(dp)
        ans = min(ans, min(dp[-1]))

    if A[0][0] + A[-1][0] <= W:
        dp = [[INF, INF, INF, INF] for _ in range(N)]
        dp[0][1] = 2
        dp = fill_table(dp)
        ans = min(ans, min(dp[-1][2], dp[-1][3]) - 1)

    if A[0][1] + A[-1][1] <= W:
        dp = [[INF, INF, INF, INF] for _ in range(N)]
        dp[0][2] = 2
        dp = fill_table(dp)
        ans = min(ans, min(dp[-1][1], dp[-1][3]) - 1)

    if A[0][0] + A[-1][0] <= W and A[0][1] + A[-1][1] <= W:
        dp = [[INF, INF, INF, INF] for _ in range(N)]
        dp[0][0] = 2
        dp = fill_table(dp)
        ans = min(ans, dp[-1][3] - 2)

    print(ans)
