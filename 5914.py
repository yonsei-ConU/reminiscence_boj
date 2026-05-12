import sys
from functools import cmp_to_key
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def cmp(a, b):
    t = 0
    for i in range(5):
        if order[i][a] > order[i][b]:
            t += 1
        elif order[i][a] == order[i][b]:
            assert False
    if t >= 3:
        return 1
    else:
        return -1


N = int(input_())
order = []

for i in range(5):
    lst = [int(input_()) for _ in range(N)]
    lst_rev = {}
    for j, v in enumerate(lst):
        lst_rev[v] = j
    order.append(lst_rev)

for element in sorted(lst, key=cmp_to_key(cmp)):
    print(element)
