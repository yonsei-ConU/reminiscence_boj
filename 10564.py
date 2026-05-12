# 19m 18:17s + 2wa

import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    N, M = minput()
    S = list(minput())
    t = max(S)
    a = b = 0
    while b <= N:
        a += t
        b += a
    a, b = b, a
    # dp[i][j]: 팔굽혀펴기 한 횟수 i, 점수 j 도달가능여부
    dp = [[False] * b for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N + 1):
        for j in range(b):
            if not dp[i][j]: continue
            for s in S:
                if i + j + s > N or j + s >= b: continue
                dp[i + j + s][j + s] = True

    for j in range(b)[::-1]:
        if dp[N][j]:
            print(j)
            break
    else:
        print(-1)
