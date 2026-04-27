import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class RNG:
    def __init__(self, r, s, m, x):
        self.r = r
        self.s = s
        self.m = m
        self.x = x
        self.c = 0

    def get_random(self):
        tmp = self.x[-self.s] - self.x[-self.r] - self.c
        ret = tmp % self.m
        self.c = +(tmp < 0)
        self.x.popleft()
        self.x.append(ret)
        return ret


def left(cur):
    ret = []
    score = 0
    for c in cur:
        if ret and ret[-1] == c:
            c *= 2
            score += c
            ret.pop()
        ret.append(c)
    return ret, score


def right(cur):
    x, y = left(cur[::-1])
    return x[::-1], y


for _ in range(int(input_())):
    input_()
    n = int(input_())
    board = [sum(list(minput()))]
    rng = RNG(43, 22, 2**32, deque(list(minput())))
    ans = 0
    while True:
        rng.get_random()
        nxt, score = left(board)
        if board == nxt and len(nxt) == n:
            break
        board, nxt = nxt, board
        ans += score
        t = rng.get_random()
        if not t % 10:
            board.append(4)
        else:
            board.append(2)
    print(ans)
