import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


Q = int(input_())
problems = 0
ans = True

for _ in range(Q):
    x, y = minput()
    if x == 1:
        problems += y
    else:
        problems -= y
    if problems < 0:
        ans = False

if ans:
    print('See you next month')
else:
    print('Adios')
