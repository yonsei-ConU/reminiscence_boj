import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = M = 3
for i in list(range(16)) + list(range(512-16, 512)):
    q = deque([i])
    visited = [False] * 512
    m = i
    while q:
        cur = q.popleft()
        for nxt_ in [0b11011, 0b110110, 0b11011000, 0b110110000]:
            nxt = cur ^ nxt_
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                m = min(m, nxt)
    print(m)

"""N = M = 4
q = deque([0])
visited = [False] * 65536
while q:
    cur = q.popleft()
    for nxt_ in [0b110011, 0b1100110, 0b11001100, 0b1100110000, 0b11001100000, 0b110011000000, 0b11001100000000, 0b110011000000000, 0b1100110000000000]:
        nxt = cur ^ nxt_
        if not visited[nxt]:
            q.append(nxt)
            visited[nxt] = True

print([i for i in range(65536) if visited[i]])
print(sum(visited))"""
