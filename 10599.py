import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    a, b, c, d = minput()
    if a == b == c == d:
        break
    print(c - b, d - a)
