import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def bf():
    for x0 in range(N + 1):
        for y0 in range(M + 1):
            for x1 in range(N + 1):
                for y1 in range(M + 1):
                    if abs(x0 * y1 - x1 * y0) == A:
                        return x0, y0, x1, y1
    return 0, 0, 0, 0


for i in range(1, int(input_()) + 1):
    N, M, A = minput()
    if A > N * M:
        print(f"Case #{i}: IMPOSSIBLE")
    else:
        rx0, ry0, rx1, ry1 = bf()
        if rx0 == ry0 == rx1 == ry1 == 0:
            print(f"Case #{i}: IMPOSSIBLE")
        else:
            print(f"Case #{i}:", 0, 0, rx0, ry0, rx1, ry1)
