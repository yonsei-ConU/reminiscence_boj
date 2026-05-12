import sys
from algorithms import bootstrap
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


@bootstrap
def dfs(cur):
    for nxt in children[cur]:
        yield dfs(nxt)
        if dp[nxt][1] > 0:
            dp[cur][0] += dp[nxt][1]
            trace[cur][0].append((nxt, 1))
        if max(dp[nxt]) > 0:
            dp[cur][1] += max(dp[nxt])
            if max(dp[nxt]) == dp[nxt][0]:
                trace[cur][1].append((nxt, 0))
            else:
                trace[cur][1].append((nxt, 1))
    dp[cur][0] += nalari[cur]
    yield


def backtrack(stack):
    ret = []
    while stack:
        cur, inex = stack.pop()
        if not inex:
            ret.append(cur + 1)
        for nxt in trace[cur][inex]:
            stack.append(nxt)
    return sorted(ret)


N = int(input_())
nalari = list(minput())
par = list(minput())
children = [[] for _ in range(N)]

for i in range(1, N):
    children[par[i - 1] - 1].append(i)

# 0은 자신을 포함, 1은 자신을 미포함
dp = [[0, 0] for _ in range(N)]
trace = [[[], []] for _ in range(N)]
dfs(0)
print(*dp[0])
ans = backtrack([(0, 0)])
ans.append(-1)
print(*ans)
ans = backtrack([(0, 1)])
ans.append(-1)
print(*ans)
