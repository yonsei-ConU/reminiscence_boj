import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

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
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


# 아래 위 오른쪽 왼쪽
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# STEP 0: 입력 O(MN)
N, M = minput()
piet = [input_().rstrip() for _ in range(N)]

# STEP 1: 블록들을 뽑아냄 amortized O(NMalpha(NM))
uf = UnionFind(N * M)
visited = [[False] * M for _ in range(N)]
blocks = []
for y in range(N):
    for x in range(M):
        if visited[y][x]: continue
        elif piet[y][x] == 'X':
            visited[y][x] = True
            continue
        q = deque([(y, x)])
        visited[y][x] = True
        blocks.append([])
        blocks[-1].append((y, x))
        while q:
            cy, cx = q.popleft()
            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                if (not (0 <= ny < N and 0 <= nx < M)) or visited[ny][nx] or piet[ny][nx] != piet[cy][cx] or piet[ny][nx] == 'X': continue
                q.append((ny, nx))
                blocks[-1].append((ny, nx))
                uf.union(cy * M + cx, ny * M + nx)
                visited[ny][nx] = True

# STEP 2: 각 블록들의 끝값들을 뽑아냄 amortized O(NM)
# [y최소, y최대, x최소, x최대]
block_end_values = []
for block in blocks:
    min_y_val = min(block, key=lambda pos: pos[0])[0]
    max_y_val = max(block, key=lambda pos: pos[0])[0]
    min_x_val = min(block, key=lambda pos: pos[1])[1]
    max_x_val = max(block, key=lambda pos: pos[1])[1]
    min_y_coords = []
    max_y_coords = []
    min_x_coords = []
    max_x_coords = []
    for y, x in block:
        if y == min_y_val:
            min_y_coords.append((y, x))
        if y == max_y_val:
            max_y_coords.append((y, x))
        if x == min_x_val:
            min_x_coords.append((y, x))
        if x == max_x_val:
            max_x_coords.append((y, x))

    min_y_coords = [max(min_y_coords, key=lambda pos: pos[1]), min(min_y_coords, key=lambda pos: pos[1])]
    max_y_coords = [min(max_y_coords, key=lambda pos: pos[1]), max(max_y_coords, key=lambda pos: pos[1])]
    min_x_coords = [min(min_x_coords, key=lambda pos: pos[0]), max(min_x_coords, key=lambda pos: pos[0])]
    max_x_coords = [max(max_x_coords, key=lambda pos: pos[0]), min(max_x_coords, key=lambda pos: pos[0])]
    # 아래 위 오른쪽 왼쪽 맞추기
    block_end_values.append([max_y_coords, min_y_coords, max_x_coords, min_x_coords])

# STEP 3: 블록 좌표가 주어지면 유파 이용해 시간 줄이는 전처리 O(블록개수*alpha(블록개수))
find_to_idx = {}
for i in range(len(blocks)):
    y, x = blocks[i][0]
    t = y * M + x
    find_to_idx[uf.find(t)] = i

# STEP 4: 이제진짜시뮬레이션
y = x = 0
# dp값은 dy,dx 인덱스
dp = 2
next_dp = [3, 2, 0, 1]
# cc값은 오른쪽이면 0 왼쪽이면 1
cc = 1

output = []
while True:
    output.append(piet[y][x])
    cnt = 0
    chk = False
    while not chk:
        ny, nx = block_end_values[find_to_idx[uf.find(y * M + x)]][dp][cc]
        ny, nx = ny + dy[dp], nx + dx[dp]
        if (not (0 <= ny < N and 0 <= nx < M)) or piet[ny][nx] == 'X':
            if not cnt & 1:
                cc ^= 1
            else:
                dp = next_dp[dp]
            cnt += 1
            if cnt == 8:
                chk = True
        else:
            chk = True
    if cnt == 8:
        break
    else:
        y, x = ny, nx

print(''.join(output))
