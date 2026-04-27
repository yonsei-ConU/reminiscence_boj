import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


mod = 10 ** 9 + 7
N, K = minput()
if not K:
    fib = [0, 1, 1, 2]
    for i in range(100000): fib.append((fib[-1] + fib[-2]) % mod)
    fib[3] = 1
    exit(print(fib[N + 2]))

# 여기부터 시작
# dp[i][j][k][l] = (i번째 문제까지, A가 해결한 문제 수 = j (mod K), 직전에 푼 사람이 B이다 아니다, C가 문제 풀었다)
dp = [[[0, 0] for _ in range(2)] for __ in range(K)]
dp[0][0][0] = 1
for i in range(N):
    nxt = [[[0, 0] for _ in range(2)] for __ in range(K)]
    for j in range(K):
        for k in range(2):
            for l in range(2):
                # case1. A solve
                nxt[(j + 1) % K][0][l] += dp[j][k][l]
                # case2. B solve
                if not k:
                    nxt[j][1][l] += dp[j][k][l]
                # case3. C solve
                nxt[j][0][1] += dp[j][k][l]
    dp, nxt = nxt, dp

ans = dp[0][0][1] + dp[0][1][1]
if ans >= mod:
    ans -= mod
print(ans)
