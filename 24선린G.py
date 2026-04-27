import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
a, b = minput()
ans = [['' for _ in range(M)] for __ in range(N)]

for i in range(N):
    for j in range(M):
        if i <= a - 2:
            d = 'S'
        elif i >= a + 2:
            d = 'N'
        elif i == a - 1 and j == b:
            d = 'S'
        elif i == a + 1 and j == b:
            d = 'N'
        elif j < b:
            d = 'E'
        elif j > b:
            d = 'W'
        else:
            assert i == a and j == b
            d = 'E'
        ans[i][j] = d

for p in ans: print(''.join(p))
