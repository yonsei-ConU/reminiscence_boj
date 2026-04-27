import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dp = [[] for _ in range(11)]
for i in range(1, 11):
    # dp[i][mask] = K == i, 남은거 집합 mask인 상태를 내가 잡으면 승패
    dp[i] = [0] * (1 << i)
    for mask in range(1, 1 << i):
        for j in range(i):
            if mask & (1 << j) and not dp[i][mask ^ (1 << j)]:
                dp[i][mask] = 1
                break

sum_to_mask = [[] for _ in range(56)]
for mask in range(1024):
    t = 0
    for j in range(10):
        if mask & (1 << j):
            t += j + 1
    sum_to_mask[t].append(mask)

for _ in range(int(input_())):
    A, B, K = minput()
    diff = (B - A) % ((K * (K + 1)) >> 1)
    chk = False
    for v in sum_to_mask[diff]:
        if v >= len(dp[K]):
            break
        elif dp[K][v]:
            chk = True
            break
    if chk:
        print("swoon")
    else:
        print("raararaara")
