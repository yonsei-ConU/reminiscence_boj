import sys
from collections import defaultdict, deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
cnt = {}
for _ in range(M):
    x, c = minput()
    cnt[x] = c
g = defaultdict(list)
keys = list(cnt.keys())
indegree = {x: 0 for x in keys}
for i in range(M):
    for j in range(M):
        if i == j:
            continue
        elif not keys[i] % keys[j]:
            g[keys[i]].append(keys[j])
            indegree[keys[j]] += 1

# dp[i][j]: 마지막 수가 i이고 사용한 수 개수가 j일 때 합의 최댓값
dp = {x: [0] * (N + 1) for x in keys}
tmp = {x: [0] * (N + 1) for x in keys}
zero_indegree = deque([x for x in indegree if not indegree[x]])
while zero_indegree:
    cur = zero_indegree.popleft()
    for i in range(1, N + 1):
        j = min(cnt[cur], i)
        if i == j or tmp[cur][i - j]:
            dp[cur][i] = max(dp[cur][i], tmp[cur][i - j] + cur * j)
    for nxt in g[cur]:
        for i in range(N + 1):
            tmp[nxt][i] = max(tmp[nxt][i], dp[cur][i])
        indegree[nxt] -= 1
        if not indegree[nxt]:
            zero_indegree.append(nxt)

ans = -1
for value in dp:
    if dp[value][N] > 0:
        ans = max(ans, dp[value][N])
print(ans)
