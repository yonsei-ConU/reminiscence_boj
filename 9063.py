import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
x = y = 20000
X = Y = -20000
for _ in range(N):
    tx, ty = minput()
    x = min(x, tx)
    y = min(y, ty)
    X = max(X, tx)
    Y = max(Y, ty)

print((Y - y) * (X - x))
