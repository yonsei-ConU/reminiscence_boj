import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, M = minput()
if N >= M:
    print(0)
else:
    ans = 1
    for i in range(2, N+1):
        ans = ans * i % M
    print(ans)
