import sys
from types import GeneratorType
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


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
def dfs(cur):
    next_state = set()
    for nxt in child[cur]:
        yield dfs(nxt)
        next_state.add(grundy[nxt])
    mex = 0
    while mex in next_state:
        mex += 1
    grundy[cur] = mex
    yield


for tc in range(1, int(input_()) + 1):
    N = int(input_())
    M = list(minput())
    par = list(minput())
    child = [[] for _ in range(N)]
    for i in range(1, N):
        child[par[i] - 1].append(i)
    grundy = [0] * N
    dfs(0)
    ans = 0
    for i in range(N):
        if M[i] % 2:
            ans ^= grundy[i]
    print(f"Case #{tc}: {'sfeicrosntd'[bool(ans)::2]}")
