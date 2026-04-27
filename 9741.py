import sys
from fractions import Fraction
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    l = list(minput())
    points = [(l[0], l[1]), (l[2], l[3]), (l[4], l[5])]
    points.sort()
    A, B, C = points
    if (B[1] - A[1]) * (C[0] - B[0]) == (B[0] - A[0]) * (C[1] - B[1]):
        print(0)
        continue
    try:
        AB = lambda x: Fraction(B[1] - A[1]) / Fraction(B[0] - A[0]) * (x - A[0]) + A[1]
    except:
        AB = 'I am coding noob'
    try:
        BC = lambda x: Fraction(C[1] - B[1]) / Fraction(C[0] - B[0]) * (x - B[0]) + B[1]
    except:
        BC = 'I am coding noob'
    try:
        AC = lambda x: Fraction(C[1] - A[1]) / Fraction(C[0] - A[0]) * (x - C[0]) + C[1]
    except:
        AC = 'I am coding noob'
        assert 0
    ans = 0
    for i in range(A[0] + 1, C[0]):
        if i <= B[0]:
            p = AB(i)
            q = AC(i)
        else:
            p = BC(i)
            q = AC(i)
        up, down = max(p, q), min(p, q)
        if up == int(up):
            up = int(up) - 1
        else:
            up = int(up)
        down = int(down) + 1
        ans += up - down + 1
    print(ans)
