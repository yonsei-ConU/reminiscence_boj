import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

a, b = minput()
if a in [1, 3, 4]:
    A = -1
else:
    A = a
if b in [1, 3, 4]:
    B = -1
else:
    B = b
if A != -1 and B == -1:
    print('>')
elif A == -1 and B != -1:
    print('<')
elif A == B:
    print('=')
elif (A, B) in ((0, 2), (2, 5), (5, 0)):
    print('>')
else:
    print('<')
