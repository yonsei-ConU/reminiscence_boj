import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, K = minput()
K -= 1
games_left = []
teams_left = set()
scores = [0] * N
X = 0
for i in range(M):
    t1, t2, result = minput()
    t1 -= 1; t2 -= 1
    if not result:
        games_left.append((t1, t2))
        teams_left |= {t1, t2}
        X += 1
    elif result == 1:
        scores[t1] += 1
    else:
        scores[t2] += 1

max_score = max(scores)
max_score_count = scores.count(max_score)
teams_left = {x: scores[x] for x in teams_left}
ans = 0
for mask in range(1 << X):
    temp_scores = teams_left.copy()
    for i in range(X):
        if mask & (1 << i):
            temp_scores[games_left[i][1]] += 1
        else:
            temp_scores[games_left[i][0]] += 1
    chk = False
    max_idx = -1
    max_val = 0
    for idx in temp_scores:
        if temp_scores[idx] > max_val:
            max_val = temp_scores[idx]
            max_idx = idx
            chk = True
        elif temp_scores[idx] == max_val:
            chk = False
    if (max_idx != K and max_val < max_score and scores[K] == max_score) or (max_idx == K and max_val > max_score and chk) or (max_idx == K and max_score == max_val and chk and max_score_count == 1):
        ans += 1

print(ans)
