import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans = N
M = int(input_())
sweep = set()
for _ in range(M):
    x, y = minput()
    sweep.add((x, y))

sweep = sorted(sweep)
start = 0
end = 0
for i in range(M):
    s, e = sweep[i]
    if s <= end:
        end = max(end, e)
    else:
        ans -= end - start
        end = e
        start = s

ans -= end - start
print(ans)
