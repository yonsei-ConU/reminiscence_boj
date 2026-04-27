import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    i, f = minput()
    if (i, f) in ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)):
        print("Yes")
    else:
        print("No")
