import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def calc_grundy(x):
    if not x or x == 2:
        return 0
    elif x % 2:
        return (x + 1) >> 1
    else:
        return (x - 2) >> 1


N = int(input_())
P = list(minput())
P = map(calc_grundy, P)
ans = 0
for g in P:
    ans ^= g

print(['cubelover', 'koosaga'][bool(ans)])
