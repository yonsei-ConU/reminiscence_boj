import sys
sys.setrecursionlimit(100001)
from heapq import heappop as pop, heappush as push
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def asdf(x):
    while miss[x][0] != INF and tier[miss[x][0]] < 3:
        pop(miss[x])
    s = second[x][0]
    m = miss[x][0]
    if s < m:
        # second 먹던애가 first 먹음
        tier[s] = 1
        nxt = cereal[pop(second[x])][1]
        eaten[nxt] = False
        return asdf(nxt)
    elif m != INF:
        global ans
        ans += 1
        if cereal[m][0] == x:
            # 못먹던애가 1지망먹음
            tier[m] = 1
        else:
            assert cereal[m][1] == x
            tier[m] = 2
            push(second[cereal[m][0]], x)
        pop(miss[x])


INF = 99999999
N, M = minput()
cereal = [list(minput()) for _ in range(N)]
eaten = [False] * M
tier = [0] * N
second = [[INF] for _ in range(M)]
miss = [[INF] for _ in range(M)]
ans = 0
for i in range(N):
    f, s = cereal[i]
    f -= 1; s -= 1
    if not eaten[f]:
        eaten[f] = True
        tier[i] = 1
        ans += 1
    elif not eaten[s]:
        eaten[s] = True
        tier[i] = 2
        ans += 1
        push(second[f], i)
    else:
        tier[i] = 3
        push(miss[f], i)
        push(miss[s], i)

print(ans)
print(tier)
for i in range(N - 1):
    if tier[i] != 1: assert False
    ans -= 1
    x = cereal[i][0]
    asdf(x)
    print(ans)
    print(tier)
