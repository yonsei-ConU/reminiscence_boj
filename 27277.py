import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
a = list(minput())
a.sort()
m, p = a[:N//2], a[N//2:]
assert len(p) - len(m) in [0, 1]
print(sum(p) - sum(m) + (a[N//2-1] if not N % 2 else 0))
