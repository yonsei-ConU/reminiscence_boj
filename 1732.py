import sys
from fractions import Fraction
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
buildings = defaultdict(list)

for _ in range(N):
    x, y, z = minput()
    assert x ** 2 + y ** 2
    if not x:
        if y > 0:
            buildings[(10 ** 18, 1)].append((x, y, z))
        else:
            buildings[(10 ** 18, -1)].append((x, y, z))
    else:
        if x > 0:
            buildings[(Fraction(y) / Fraction(x), 1)].append((x, y, z))
        else:
            buildings[(Fraction(y) / Fraction(x), -1)].append((x, y, z))

res = []
for same_incl_and_sign in buildings:
    MoongTaengE = buildings[same_incl_and_sign]
    MoongTaengE.sort(key=lambda x: (abs(x[0]), abs(x[1])))
    highest = -1
    for x, y, height in MoongTaengE:
        if height > highest:
            highest = height
        else:
            res.append((x, y))

for x, y in sorted(res):
    print(x, y)
