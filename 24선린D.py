import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
glass = list(map(int, list(input_().rstrip())))
streak = 0
ans = []

for i in range(N):
    if glass[i]:
        streak += 1
    else:
        ans.append(streak)
        streak = 0

ans.append(streak)
print(sum((x * (x + 1)) >> 1 for x in ans))
