import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def edmond_karp(capacity, source, sink):
    from collections import deque
    N = len(capacity)
    ret = 0

    while 1:
        parent = [None] * N
        parent[source] = source
        q = deque([source])
        while q and parent[sink] is None:
            cur = q.popleft()
            for nxt in range(N):
                if capacity[cur][nxt] is not None and capacity[cur][nxt] and parent[nxt] is None:
                    q.append(nxt)
                    parent[nxt] = cur

        if parent[sink] is None:
            break

        amount = float('inf')
        cur = sink
        while cur != source:
            nxt = parent[cur]
            amount = min(amount, capacity[nxt][cur])
            cur = nxt

        ret += amount
        cur = sink
        while cur != source:
            nxt = parent[cur]
            capacity[nxt][cur] -= amount
            capacity[cur][nxt] += amount
            cur = nxt

    return ret


N, P = minput()
capacity = [[None] * N for _ in range(N)]
for _ in range(P):
    s, e = minput()
    s -= 1; e -= 1
    capacity[s][e] = 1
    capacity[e][s] = 0

print(edmond_karp(capacity, 0, 1))
