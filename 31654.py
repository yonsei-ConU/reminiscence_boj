import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


A, B, C = minput()
if A + B == C:
    print('correct!')
else:
    print('wrong!')
