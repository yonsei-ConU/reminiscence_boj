import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
g = [set() for _ in range(N)]
for _ in range(M):
    a, b = minput()
    a -= 1; b -= 1
    g[a].add(b)
    g[b].add(a)

ans = 0
for mask in range(1 << N):
    chk = True
    impossible = set()
    for i in range(N):
        if mask & (1 << i):
            if i in impossible:
                chk = False
                break
            impossible |= g[i]
    ans += chk

print(ans)
