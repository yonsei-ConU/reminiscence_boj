import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


a, b, c = minput()
s = sum([a, b, c])
m = max(a, b, c)
if s - m > m:
    print(s)
else:
    print((s - m) * 2 - 1)
