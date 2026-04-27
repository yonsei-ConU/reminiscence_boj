import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

n = int(input_())
w = list(minput())
result = []
ans = 123456
for i in range(n):
    ans += 1
    if w[i] < ans:
        ans = w[i]
    result.append(ans)

print(*result)
