import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, M, K = minput()
scores = [0] * (N + 1)
ongoing = []
not_finished_teams = set()
for i in range(M):
    a, b, c = minput()
    if c == 1:
        scores[a] += 1
    elif c == 2:
        scores[b] += 1
    else:
        ongoing.append([a, b])
        not_finished_teams |= {a, b}

ans = 0
max_score = max(scores)
scores_important = {i: scores[i] for i in not_finished_teams}
scores_important[K] = scores[K]
for mask in range(1 << len(ongoing)):
    si = scores_important.copy()
    for i in range(len(ongoing)):
        si[ongoing[i][bool(mask & 1 << i)]] += 1
    if si[K] <= max_score:
        continue
    for i in si:
        if i != K and si[i] >= si[K]:
            continue
    ans += 1

print(ans)
