import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())

plus = []
minus = []

for i in range(N):
    x, y = minput()
    plus.append(x + y)
    minus.append(x - y)

print(max(max(plus) - min(plus), max(minus) - min(minus)))
