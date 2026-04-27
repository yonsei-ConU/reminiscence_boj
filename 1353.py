from math import e, log

p, q = map(int, input().split())
r = 1

if p / e < log(q):
    print(-1)
elif p == q:
    print(1)
elif p > q:
    print(2)
else:
    while True:
        s = (p / r) ** r
        if s >= q:
            print(r)
            break
        r += 1
