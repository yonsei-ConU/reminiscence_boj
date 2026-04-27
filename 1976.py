import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


from collections import deque
N = int(input_())
M = int(input_())
city = [list(minput()) for _ in range(N)]
plan = list(map(lambda x: int(x) - 1, input_().split()))
q = deque([plan[0]])
plan = set(plan)
plan.remove(q[0])
visited = [False] * N
visited[q[0]] = True

while q:
    cur = q.popleft()
    for nxt in range(N):
        if city[cur][nxt] and not visited[nxt]:
            q.append(nxt)
            visited[nxt] = True
            if nxt in plan: plan.remove(nxt)

print("YNEOS"[bool(plan)::2])            
