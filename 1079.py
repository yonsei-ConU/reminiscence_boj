import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dfs(night, alive):
    global ans
    t = bin(alive).count('1')
    if t == 2:
        ans = max(ans, night)
        return
    dead = set()
    for p in range(N):
        if not alive & (1 << p): dead.add(p)
    for nxt in range(N):
        if nxt == dmswls or nxt in dead: continue
        # nxt번을 죽인다
        dead.add(nxt)
        idx = -1
        val = -100000
        for i in range(N):
            if i in dead: continue
            guilty[i] += R[nxt][i]
            if guilty[i] > val:
                val = guilty[i]
                idx = i
        if idx == dmswls:
            ans = max(ans, night)
        else:
            dfs(night + 1, alive ^ (1 << nxt) ^ (1 << idx))
        for i in range(N):
            if i in dead: continue
            guilty[i] -= R[nxt][i]
        dead.remove(nxt)


N = int(input_())
guilty = list(minput())
R = [list(minput()) for _ in range(N)]
dmswls = int(input_())
alive = (1 << N) - 1
if N % 2:
    idx = -1
    val = -100000
    for i in range(N):
        if guilty[i] > val:
            val = guilty[i]
            idx = i
    if idx == dmswls:
        exit(print(0))
    else:
        alive ^= 1 << idx
ans = 0
dfs(1, alive)
print(ans)
