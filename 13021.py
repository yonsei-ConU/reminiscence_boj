import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
balls = [0] * N
for i in range(1, M + 1):
    L, R = minput()
    L -= 1
    R -= 1
    for j in range(L, R + 1):
        balls[j] = i

balls = set(balls)
ans = len(balls)
if 0 in balls: ans -= 1
print(2 ** ans)
