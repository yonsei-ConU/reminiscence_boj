import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

u, v = minput()
A = input_().rstrip()
B = input_().rstrip()
if len(A) >= 22:
    if u > v:
        print('ras')
    elif u < v:
        print('auq')
    else:
        if A > B:
            print('ras')
        elif A < B:
            print('auq')
        else:
            print('rasauq')
else:
    A = int(A, u)
    B = int(B, v)
    if A > B:
        print('ras')
    elif A < B:
        print('auq')
    else:
        print('rasauq')
