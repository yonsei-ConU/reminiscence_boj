import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
fires = []

ans_const = 0

for _ in range(n):
    a, b = minput()
    if not a:
        ans_const += b
    else:
        fires.append((b / a, a, b))

fires.sort()
ans = 0

for _, a, b in fires:
    ans += a * ans + b
    ans %= 40000

print((ans + ans_const) % 40000)
