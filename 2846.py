import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans = 0
P = list(minput())
start = last = P[0]
for p in P:
    if p <= last:
        ans = max(ans, last - start)
        start = p
    last = p

print(max(ans, last - start))
