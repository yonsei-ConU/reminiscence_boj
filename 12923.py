import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
nxt = [[] for _ in range(10000)]
for _ in range(N):
    a, b = minput()
    nxt[a].append(b)
cur = []
star = 0
ans = 0
while star < 2 * N:
    for val in nxt[star]:
        cur.append(val)
    if not cur:
        exit(print("Too Bad"))
    if min(cur) <= star:
        star += 2
        ans += 1
        for val in nxt[star - 1]:
            cur.append(val)
        cur.remove(min(cur))
    else:
        star += 1
        ans += 1
        x = max(cur)
        cur.remove(x)
        nxt[x].append(9999)

assert star == 2 * N
print(ans)
