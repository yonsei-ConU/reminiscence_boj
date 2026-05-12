import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dp(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return dp(20, 20, 20)
    elif a < b < c:
        if memo[a][b][c] is None:
            memo[a][b][c] = dp(a, b, c - 1) + dp(a, b - 1, c - 1) - dp(a, b - 1, c)
        return memo[a][b][c]
    else:
        if memo[a][b][c] is None:
            memo[a][b][c] = dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1)
        return memo[a][b][c]


memo = [[[None] * 21 for _ in range(21)] for __ in range(21)]
while True:
    a, b, c = minput()
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {dp(a, b, c)}")
