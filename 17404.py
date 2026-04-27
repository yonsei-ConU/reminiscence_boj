import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
cost = [[], [], []]
tmp = list(minput())
cost[0].append([tmp[0], 1234567, 1234567])
cost[1].append([1234567, tmp[1], 1234567])
cost[2].append([1234567, 1234567, tmp[2]])
for i in range(N - 1):
    tmp = list(minput())
    for j in range(3):
        cost[j].append(tmp)

res = 1234567890

for i in range(3):
    ans = [[0, 0, 0] for _ in range(N)]
    ans[0] = cost[i][0][:]
    for j in range(1, N):
        ans[j][0] = min(ans[j-1][1], ans[j-1][2]) + cost[i][j][0]
        ans[j][1] = min(ans[j-1][0], ans[j-1][2]) + cost[i][j][1]
        ans[j][2] = min(ans[j-1][1], ans[j-1][0]) + cost[i][j][2]
    for j in range(3):
        if i != j:
            res = min(res, ans[-1][j])

print(res)
