import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


a, b = minput()
x = a
a = (a + a % 2) // 2
a += a == 1
b = (b - b % 2) // 2
print(b * (b + 1) - a * (a - 1))
