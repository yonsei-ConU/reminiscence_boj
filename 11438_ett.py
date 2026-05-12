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
def ETT(cur, parent):
    for nxt in g[cur]:
        if nxt == parent:
            continue
        yield ETT(nxt, cur)
    for nxt in g[cur]:
        if nxt == parent:
            continue
        if len(queries[cur]) < len(queries[nxt]):
            queries[cur], queries[nxt] = queries[nxt], queries[cur]
        for element in queries[nxt]:
            if element in queries[cur]:
                output[element] = str(cur + 1)
            else:
                queries[cur].add(element)
    yield


N = int(input_())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = minput()
    u -= 1; v -= 1
    g[u].append(v)
    g[v].append(u)

queries = [set() for _ in range(N)]
M = int(input_())
output = [''] * M
for q in range(M):
    a, b = minput()
    if a == b:
        output[q] = str(a)
    else:
        queries[a - 1].add(q)
        queries[b - 1].add(q)
ETT(0, 0)

print('\n'.join(output))
