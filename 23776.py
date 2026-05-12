import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def travel(lam):
    global cur_phi, cur_lam, visited
    if abs(lam - cur_lam) != 180:
        if 0 <= lam - cur_lam < 180 or lam - cur_lam < -180:
            while lam != cur_lam:
                cur_lam += 1
                if cur_lam == 180:
                    cur_lam = -180
                visited[cur_lam * 2 + 360] = True
                visited[cur_lam * 2 + 359] = True
        else:
            while lam != cur_lam:
                cur_lam -= 1
                if cur_lam == -181:
                    cur_lam = 179
                visited[cur_lam * 2 + 360] = True
                visited[cur_lam * 2 + 361] = True
    else:
        visited = [True] * 720


n = int(input_())
# 경도 lam을 방문했다면 visited[lam * 2 + 360] == True
# visited[lam / 2 - 180] == True이면 경도 lam을 방문함
visited = [False] * 720
initial_phi, initial_lam = minput()
cur_phi, cur_lam = initial_phi, initial_lam
visited[cur_lam * 2 + 360] = True
for i in range(n - 1):
    phi, lam = minput()
    travel(lam)

travel(initial_lam)
not_visited = []
for i in range(720):
    if not visited[i]:
        not_visited.append(i / 2 - 180)

if not_visited:
    print('no', not_visited[0])
else:
    print('yes')
