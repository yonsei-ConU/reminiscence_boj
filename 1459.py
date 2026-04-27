import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


X, Y, W, S = minput()
extra = ((X + Y) & 1) * W
if extra:
    if X > Y:
        X -= 1
    else:
        Y -= 1
sum_moves = (X + Y) >> 1
diff_moves = abs(X - Y) >> 1
d = 0
ans = S * (sum_moves + diff_moves) + extra
if S > W:
    d += min(sum_moves, diff_moves)
    sum_moves -= d
    diff_moves -= d
    ans = min(ans, 2 * d * W + (sum_moves + diff_moves) * S + extra)
if S > 2 * W:
    d += max(sum_moves, diff_moves)
    ans = min(ans, 2 * d * W + extra)

print(ans)
