import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
meat = sorted([list(minput()) for _ in range(N)])
meat.sort(key=lambda x: (x[0], -x[1]))
cur = 0
ans = float('inf')

for weight, price in meat:
    cur += weight
    if cur >= M:
        ans = min(ans, price)

print(ans if ans != float('inf') else -1)
