import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, lph = minput()
loc = sorted([int(input_()) for _ in range(n)])
t = 0
ans = 0
for l in loc:
    t += l
    if t <= lph * 5:
        ans += 1
    else:
        break

print(ans)
