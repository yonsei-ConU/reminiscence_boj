import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dfs(cur):
    dp_child = []
    for nxt in children[cur]:
        dfs(nxt)
        dp_child.append(dp[nxt])
    if not dp_child:
        dp[cur] = 0
    else:
        dp_child.sort(reverse=True)
        ans = -1
        for i in range(len(dp_child)):
            ans = max(ans, dp_child[i] + i + 1)
        dp[cur] = ans


N = int(input_())
children = [[] for _ in range(N)]
par = list(minput())
for i in range(1, N):
    p = par[i]
    children[p].append(i)
dp = [10000] * N
dfs(0)
print(dp[0])
