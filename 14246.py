import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
seq = list(minput())
k = int(input_())

ps = []
t = 0
for i in range(n):
    t += seq[i]
    ps.append(t)
ans = 0

for i in range(n):
    threshold = ps[i] + k - seq[i]
    lo = -1
    hi = n
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if ps[mid] > threshold:
            hi = mid
        else:
            lo = mid
    ans += n - hi

print(ans)
