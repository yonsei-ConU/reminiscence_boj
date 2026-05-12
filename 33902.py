import sys
from math import gcd
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dp(x, y):
    if x >= y:
        return 0
    elif memo[x][y] != -1:
        return memo[x][y]
    else:
        zero = False
        for i in coprime[x]:
            if i > y:
                break
            elif not dp(i, y):
                zero = True
                break
        if zero:
            memo[x][y] = 1
        else:
            memo[x][y] = 0
        return memo[x][y]


memo = [[-1] * 1001 for _ in range(1001)]
coprime = [[] for _ in range(1001)]
for i in range(2, 1001):
    for j in range(i, 1001):
        if gcd(i, j) == 1:
            coprime[i].append(j)
X, Y = minput()
print(['putdata', 'khj20006'][dp(X, Y)])
