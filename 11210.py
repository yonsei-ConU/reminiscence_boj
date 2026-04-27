import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


m = list(minput())
x = list(minput())
y = list(minput())
for i in range(3):
    if x[i] < y[i] or x[i] + y[i] >= m[i]:
        exit(print(0))
