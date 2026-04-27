import sys
from types import GeneratorType
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
MOD = 10 ** 9 + 7


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


@bootstrap
def dfs(cur, parent):
    lst = []
    for nxt in g[cur]:
        if nxt == parent:
            continue
        yield dfs(nxt, cur)
        tmp = g[cur][nxt] * (1 + dp[nxt][0]) % MOD
        dp[cur][0] = (dp[cur][0] + tmp) % MOD
        lst.append(tmp)
    dp[cur][1] = (sum(lst) ** 2 - sum(x * x for x in lst)) >> 1
    yield


N = int(input_())
g = [{} for _ in range(N)]
for _ in range(N - 1):
    A, B, W = minput()
    A -= 1; B -= 1
    g[A][B] = W
    g[B][A] = W

# dp[i][0]: i번을 루트로 하는 서브트리에서 i번이 끝점인 경로 가중치 합
# dp[i][1]: i번을 루트로 하는 서브트리에서 i번이 끝점이 아닌 경로 가중치 합
dp = [[0, 0] for _ in range(N)]
dfs(0, 0)
print(sum(sum(d) for d in dp) % MOD)
