import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


X1, Y1, X2, Y2 = minput()
ans = 0
last = 0
for y in range(Y1, Y2):
    if y % 2:
        ans += max(0, min(y, X2) - X1)
    temp = max(X1, y)
    if temp <= X2 - 1:
        ans += (X2 - temp + temp % 2) // 2

print(ans)
