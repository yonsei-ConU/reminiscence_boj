import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def grundy(x, y):
    X = x // 12
    Y = y // 12
    delta = []
    while X | Y:
        delta.append(lst[X % 8][Y % 8])
        X >>= 3
        Y >>= 3
    return sum(delta[i] << (3 * i) for i in range(len(delta))) * 12 + lst_last[x % 12][y % 12]


lst = [[0, 1, 2, 3, 4, 5, 6, 7],
       [1, 0, 3, 2, 5, 4, 7, 6],
       [2, 3, 0, 1, 6, 7, 4, 5],
       [3, 2, 1, 0, 7, 6, 5, 4],
       [4, 5, 6, 7, 0, 1, 2, 3],
       [5, 4, 7, 6, 1, 0, 3, 2],
       [6, 7, 4, 5, 2, 3, 0, 1],
       [7, 6, 5, 4, 3, 2, 1, 0]]

lst_last = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [1, 2, 0, 4, 5, 3, 7, 8, 6, 10, 11, 9],
            [2, 0, 1, 5, 3, 4, 8, 6, 7, 11, 9, 10],
            [3, 4, 5, 0, 1, 2, 9, 10, 11, 6, 7, 8],
            [4, 5, 3, 1, 2, 0, 10, 11, 9, 7, 8, 6],
            [5, 3, 4, 2, 0, 1, 11, 9, 10, 8, 6, 7],
            [6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5],
            [7, 8, 6, 10, 11, 9, 1, 2, 0, 4, 5, 3],
            [8, 6, 7, 11, 9, 10, 2, 0, 1, 5, 3, 4],
            [9, 10, 11, 6, 7, 8, 3, 4, 5, 0, 1, 2],
            [10, 11, 9, 7, 8, 6, 4, 5, 3, 1, 2, 0],
            [11, 9, 10, 8, 6, 7, 5, 3, 4, 2, 0, 1]]


def naive():
    grundy = [[0] * 3000 for _ in range(3000)]
    for i in range(481):
        for j in range(481):
            if not i and not j: continue
            next_state = set()
            for x in range(i):
                next_state.add(grundy[x][j])
            for y in range(j):
                next_state.add(grundy[i][y])
            next_state.add(grundy[i - 1][j - 1])
            mex = 0
            while mex in next_state:
                mex += 1
            grundy[i][j] = mex
    return grundy


ans = 0
for _ in range(int(input_())):
    x, y = minput()
    ans ^= grundy(x, y)

if not ans:
    print('cubelover')
else:
    print('koosaga')
