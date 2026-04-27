import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for line in sys.stdin:
    if not line:
        break
    S, piece = line.split()
    S = int(S)
    if S == 1:
        print(1)
    elif piece == 'B':
        print(2)
    elif piece == 'R':
        print(S)
    elif piece == 'K':
        print(4)
    elif S == 2:
        print(1)
    else:
        print(2)
