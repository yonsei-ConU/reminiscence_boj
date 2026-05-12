import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, Q = minput()
sets = []
for i in range(N):
    cnt, *s = minput()
    sets.append(set(s))

for _ in range(Q):
    query = list(minput())
    if query[0] == 1:
        a, b = query[1:]
        a -= 1; b -= 1
        if len(sets[b]) > len(sets[a]):
            sets[b], sets[a] = sets[a], sets[b]
        sets[a] |= sets[b]
        sets[b] = set()
    else:
        a = query[1] - 1
        print(len(sets[a]))
