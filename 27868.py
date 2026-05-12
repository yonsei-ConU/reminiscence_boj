import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, S = minput()
S -= 1
A = list(minput())
command = input_().rstrip()
cur = S
velocity = 0
