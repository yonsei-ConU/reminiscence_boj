import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
d = list(minput())
if N == 1: print(['Unh', 'H'][not (d[0] - 1)] + 'appy')
else: print(['Unh', 'H'][sum(d) >= max(d) * 2] + 'appy')
