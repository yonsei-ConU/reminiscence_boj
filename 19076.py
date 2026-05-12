import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, K = minput()
a = sorted(list(minput()), reverse=True)
ans = 0
last = -1
for v in a:
    if last - v > K:
        break
    ans += 1
    last = v

print(ans)
