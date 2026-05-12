import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


S = set()
for _ in range(int(input_())):
    query = input_().split()
    q = query[0]
    if q == 'all':
        S = set(range(1, 21))
    elif q == 'empty':
        S = set()
    else:
        t = int(query[1])
        if q == 'add':
            S |= {t}
        elif q == 'remove' and t in S:
            S &= set(range(1, 21)) ^ {t}
        elif q == 'check':
            print(+(t in S))
        elif q == 'toggle':
            S ^= {t}
