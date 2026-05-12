import sys
input_ = sys.stdin.readline
def mfnput(): return map(float, input_().split())


while True:
    nx, ny, w = mfnput()
    w /= 2
    if not nx and not ny and not w:
        break
    ans = True

    X = sorted(list(mfnput()))
    last = 0
    chk = True
    for x in X:
        if last < x - w:
            chk = False
            break
        last = x + w
    if not chk or last < 75:
        ans = False

    Y = sorted(list(mfnput()))
    last = 0
    chk = True
    for y in Y:
        if last < y - w:
            chk = False
            break
        last = y + w
    if not chk or last < 100:
        ans = False

    if ans:
        print("YES")
    else:
        print("NO")
