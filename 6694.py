import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    N = int(input_())
    if not N: break
    s = set()
    x = 0
    y = 0
    for _ in range(N):
        X, Y = minput()
        s.add((N * X, N * Y))
        x += X
        y += Y
    ans = True
    for X, Y in s:
        print((X, Y), (2 * x - X, 2 * y - Y))
        ans = ans and (2 * x - X, 2 * y - Y) in s
    print(["This is a dangerous situation!", f"V.I.P should stay at ({x/N:.1f},{y/N:.1f})."][ans])

