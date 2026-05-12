import io, os
from types import GeneratorType
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
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
def ETT(cur):
    global time
    time += 1
    disc[cur] = time
    for nxt in g[cur]:
        yield ETT(nxt)
    esc[cur] = time
    yield


output = []

N, Q = minput()
g = [[] for _ in range(N)]
for _ in range(N - 1):
    p, c = minput()
    g[p].append(c)

time = -1
disc = [-1] * len(g)
esc = [-1] * len(g)
queries = [set() for _ in range(N)]
for q in range(Q):
    k, *v = minput()
    for u in v:
        queries[u].add(q)

os.write(1, '\n'.join(output).encode())
os._exit(0)
