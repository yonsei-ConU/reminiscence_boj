import sys
from itertools import permutations as perm
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def check_win(princess, prince):
    p1 = list(perm(princess))
    p2 = list(perm(prince))
    ans = 4
    for i in range(6):
        for k in range(6):
            ans = min(ans, sum(p1[i][j] < p2[k][j] for j in range(3)))
    return ans >= 2


while 1:
    A, B, C, X, Y = minput()
    if not A: break
    available = [True] * 53
    princess = [A, B, C]
    prince = [X, Y]
    for card in (A, B, C, X, Y):
        available[card] = False
    ans = -1
    for card in range(1, 53):
        if available[card] and check_win(princess, prince + [card]):
            ans = card
            break
    print(ans)
