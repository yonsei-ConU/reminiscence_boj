import sys
from math import sqrt, log, sin
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 1000000
x = [1]
for i in range(1, 1000001):
    x.append((x[int(i - sqrt(i))] + x[int(log(i))] + x[int(i * sin(i) * sin(i))]) % MOD)

while True:
    i = int(input_())
    if i == -1:
        break
    else:
        print(x[i])
