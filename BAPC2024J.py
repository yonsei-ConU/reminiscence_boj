import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
a = []
b = []
for i in range(n):
    x, y = minput()
    a.append(x)
    b.append(y)

if a == sorted(a) and b == sorted(b):
    print("yes")
else:
    print("no")
