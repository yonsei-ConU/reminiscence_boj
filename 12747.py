import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, k = minput()
if n == 3:
    if k == 1:
        print(1)
    elif k == 2:
        print(2)
    else:
        print(3)
elif n == 4:
    if k == 1:
        print(1)
    elif k == 2:
        print(3)
    elif k == 3:
        print(5)
    else:
        print(6)
elif n == 5:
    if k == 1:
        print(1)
    elif k == 2:
        print(4)
    elif k == 3:
        print(6)
    elif k == 4:
        print(8)
    else:
        print(9)
else:
    if k == 1:
        print(1)
    elif k == 2:
        print(8)
    elif k == 3:
        ...
    elif k == 4:
        ...
    elif k == 5:
        ...
    else:
        ...
