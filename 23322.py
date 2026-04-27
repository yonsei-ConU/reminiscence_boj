import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
a = list(minput())
m = min(a)
print(sum(a) - m * len(a), len(a) - a.count(m))
