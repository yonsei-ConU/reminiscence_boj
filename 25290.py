import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


d = []
cur = 1
for i in range(5000):
    d += [cur, cur + 1, cur + 1, cur + 1]
    cur += 2
num = [d[0]]
for i in range(1, len(d)):
    num.append(num[i - 1] + d[i])

for tc in range(1, int(input_()) + 1):
    N, K = minput()
    G = N * N - 1 - K
    if K < N - 1 or G & 1:
        print(f"Case #{tc}: IMPOSSIBLE")
        continue
    ans = []
    cur = 4 * N - 6
    while G:
        if G <= cur:
            ans.append(G)
            break
        else:
            ans.append(cur)
            G -= cur
            cur -= 8
    ans2 = []
    for a in ans:
        t = N * N - num[a // 2]
        ans2.append((t, t + a + 1))
    ans2.sort()
    print(f"Case #{tc}: {len(ans2)}")
    for a, b in ans2:
        print(a, b)
