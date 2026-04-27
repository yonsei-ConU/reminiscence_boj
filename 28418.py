import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


f = list(minput())
g = list(minput())
a, b, c = f
m, n = g
fog = [a * m * m, 2 * a * m * n + b * m, a * n * n + b * n + c]
gof = [a * m, b * m, c * m + n]
pmq = [fog[i] - gof[i] for i in range(3)]
if pmq == [0, 0, 0]:
    print("Nice")
else:
    A, B, C = pmq
    if A:
        D = B ** 2 - 4 * A * C
        if D > 0:
            print("Go ahead")
        elif D == 0:
            print("Remember my character")
        else:
            print("Head on")
    elif B:
        if C:
            print("Remember my character")
        else:
            print("Head on")
    else:
        print("Head on")
