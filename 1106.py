import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

C, N = minput()
cities = [list(minput()) for _ in range(N)]
dp = [0]

for i in range(1, 100001):
    temp = 0
    for cost, customer in cities:
        if cost <= i:
            temp = max(temp, dp[i - cost] + customer)
    if temp >= C:
        print(i)
        sys.exit()
    dp.append(temp)
