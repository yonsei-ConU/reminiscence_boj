import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())



N = int(input_())
data = [list(minput()) for _ in range(N)]
data.sort()
candidate = data[0][0] + data[0][1]
ans = data[0][1]
for a, b in data[1:]:
    candidate = max(candidate + b, a + b)
    ans = max(ans, candidate - a)

print(ans)
