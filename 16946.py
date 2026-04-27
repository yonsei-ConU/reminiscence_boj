import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.__size = [1] * size

    def size(self, x):
        return self.__size[self.find(x)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.__size[root_x] += self.__size[root_y]
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.__size[root_y] += self.__size[root_x]
            else:
                self.parent[root_y] = root_x
                self.__size[root_x] += self.__size[root_y]
                self.rank[root_x] += 1


from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, M = minput()
g = []
for _ in range(N):
    g.append(input_().rstrip())

uf = UnionFind(N * M)
visited = [False] * (N * M)

for i in range(N * M):
    y, x = i // M, i % M
    if g[y][x] == '0' and not visited[i]:
        visited[i] = True
        q = deque([(y, x)])
        while q:
            y, x = q.popleft()
            cur = y * M + x
            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if 0 <= ny < N and 0 <= nx < M and not visited[ny * M + nx]:
                    q.append((ny, nx))
                    visited[ny * M + nx] = True
                    uf.union(cur, ny * M + nx)

r = ''
for i in range(N * M):
    y, x = i // M, i % M
    cur = y * M + x
    if g[y][x] == '0':
        r += '0'
    else:
        tmp = [True] * 4
        ans = 1
        for j in range(4):
            if tmp[j]:
                ny, nx = y + dy[j] , x + dx[j]
                if 0 <= ny < N and 0 <= nx < M:
                    ans += uf.size(ny * M + nx)
                for k in range(j + 1, 4):
                    if tmp[k] and 0 <= ny < N and 0 <= nx < M and 0 <= y + dy[k] < N and 0 <= x + dx[k] < M and uf.find(ny * M + nx) == uf.find((y + dy[k]) * M + (x + dx[k])):
                        tmp[k] = False
        r += str(ans % 10)

for i in range(0, N * M, M):
    print(r[i:i + M])
