import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def bootstrap(f, stack=[]):
    from types import GeneratorType
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


def ETT(g, root):
    time = 0
    disc = [-1] * len(g)
    esc = [-1] * len(g)

    @bootstrap
    def ETT_process(cur, parent):
        nonlocal time
        time += 1
        disc[cur] = time
        for nxt in g[cur]:
            if nxt == parent:
                continue
            yield ETT_process(nxt, cur)
        time += 1
        esc[cur] = time
        yield
    ETT_process(root, -1)
    return disc, esc


N = int(input_())
g = [[] for _ in range(N)]
for _ in range(N):
    l = list(minput())
    u = l[0] - 1
    for v in l[1:-1]:
        g[u].append(v - 1)

for i in range(N):
    g[i].sort()

disc, esc = ETT(g, int(input_()) - 1)
for i in range(N):
    print(i + 1, disc[i], esc[i])
