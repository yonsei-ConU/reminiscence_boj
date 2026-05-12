import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while 1:
    N, M, P = minput()
    if N == M == P == 0:
        break
    X = [int(input_()) for _ in range(N)]
    s = sum(X) * 100
    m = X[M - 1]
    print(int(s * (100 - P) / 100 / m) if m else 0)
