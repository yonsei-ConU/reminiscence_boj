import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    # 다 채울 수 있으면 G, 아니면 R
    x, R, C = minput()
    if R < C:
        R, C = C, R
    # WLOG, R >= C
    if x >= 7:
        win = 'RICHARD'
    elif x == 1:
        win = 'GABRIEL'
    elif x == 2:
        if (R * C) & 1 or R < 2:
            win = 'RICHARD'
        else:
            win = 'GABRIEL'
    elif x == 3:
        if (R * C) % 3 or R < 3 or C == 1:
            win = 'RICHARD'
        else:
            win = 'GABRIEL'
    elif x == 4:
        if (R * C) & 3 or R < 4 or C <= 2:
            win = 'RICHARD'
        else:
            win = 'GABRIEL'
    elif x == 5:
        if (R * C) % 5 or R < 5 or C <= 2 or (R == 5 and C <= 3):
            win = 'RICHARD'
        else:
            win = 'GABRIEL'
    else:
        if (R * C) % 6 or R < 6 or C <= 3:
            win = 'RICHARD'
        else:
            win = 'GABRIEL'
    print(f"Case #{tc}: {win}")
