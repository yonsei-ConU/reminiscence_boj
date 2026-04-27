import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def xor(x):
    return [x, 1, x + 1, 0][x & 3]


for _ in range(int(input_())):
    S, F = minput()
    print(xor(F) ^ xor(S - 1))
