import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


from collections import deque

for _ in range(int(input_())):
    V, E = minput()
    g = [[] for _ in range(V)]
    for _ in range(E):
        u, v = minput()
        u -= 1; v -= 1
        g[u].append(v)
        g[v].append(u)
    visited = [0] * V
    ans = True
    for i in range(V):
        if not visited[i]:
            q = deque([i])
            visited[i] = 1
            while q:
                cur = q.popleft()
                color = visited[cur]
                for nxt in g[cur]:
                    if visited[nxt] == color:
                        ans = False
                        q = False
                        break
                    elif not visited[nxt]:
                        visited[nxt] = -color
                        q.append(nxt)
            if not ans:
                break
    print('YNEOS'[1-ans::2])
