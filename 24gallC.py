import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, H, S = minput()
f = list(minput())

ans1 = sum(f[i] * (2 * i + 1) for i in range(N))
ans2 = sum(f[N - 1 - i] * (2 * i + 1) for i in range(N))
d = sum(f[i] * max(0, S - N * H / 2) for i in range(N))
ans = min(ans1, ans2)
print((ans * min(S, N * H / 2) + d) / N / N)
