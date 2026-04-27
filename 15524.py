import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dist_point_line_sq(p, line):
    x0, y0 = p
    (x1, y1), (x2, y2) = line
    return ((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1)) ** 2 / ((x2 - x1) ** 2 + (y2 - y1) ** 2)


def dist_point_point_sq(p1, p2):
    return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2


def dot(a, b, c):
    ba = (a[0] - b[0], a[1] - b[1])
    bc = (c[0] - b[0], c[1] - b[1])
    return ba[0] * bc[0] + ba[1] * bc[1] >= 0


N = int(input_())
coins = [list(minput()) for _ in range(N)]
# dp[mask] = 옮겨진 동전 집합이 mask인 경우가 도달 가능한가?
# 비트가 1이면 동전이 옮겨진 상태, 0이면 옮겨지지 않은 상태
dp = [False] * (1 << N)
dp[0] = True
ans = 0
# 시복도 N**2 * 2**N
for mask in range(1 << N):
    if not dp[mask]: continue
    for i in range(N):
        # i번동전을 옮기지 않은 경우
        if not mask & (1 << i):
            # 옮기는 게 가능한지 확인
            # 점 s와 점 t를 잇는 직선을 구함
            line = [[coins[i][1], coins[i][2]], [coins[i][3], coins[i][4]]]
            chk = True
            # 다른 모든 중심에 대해 점과 직선 사이 거리를 구함
            for j in range(N):
                if j == i: continue
                if mask & (1 << j):
                    center = [coins[j][3], coins[j][4]]
                else:
                    center = [coins[j][1], coins[j][2]]
                if not (dot(center, line[0], line[1]) and dot(center, line[1], line[0])):
                    dist_sq = min(dist_point_point_sq(center, coins[i][1:3]), dist_point_point_sq(center, coins[i][3:]))
                else:
                    dist_sq = dist_point_line_sq(center, line)
                if dist_sq <= (coins[i][0] + coins[j][0]) ** 2:
                    chk = False
                    break
            if chk:
                dp[mask | (1 << i)] = True
                ans = max(ans, mask.bit_count() + 1)

print(ans)
