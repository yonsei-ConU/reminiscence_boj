import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, L = minput()
ude = sorted([tuple(minput()) for _ in range(N)])
last = -1
ans = 0
for s, e in ude:
    s = max(s, last)
    last = max(s, last)
    delta = (e - s + L - 1) // L
    ans += delta
    last += delta * L

print(ans)
