import sys
from fractions import Fraction
from decimal import Decimal
input_ = sys.stdin.readline
def minput(): return map(Fraction, input_().split())


while True:
    hx1, hx2, hy = minput()
    if not hx1 and not hx2 and not hy:
        break
    px1, px2, py = minput()
    hy -= py
    impossible = []
    for _ in range(int(input_())):
        x1, x2, y = minput()
        y -= py
        if not (0 < y < hy):
            continue
        left = (hy * x1 - y * hx2) / (hy - y)
        right = (hy * x2 - y * hx1) / (hy - y)
        if right < px1 or left > px2:
            continue
        if left < px1:
            left = px1
        if right > px2:
            right = px2
        impossible.append((float(left), float(right)))

    if not impossible:
        ans = px2 - px1
    else:
        impossible.sort()
        merged = []
        cur_start, cur_end = impossible[0]
        for start, end in impossible[1:]:
            if start > cur_end:
                merged.append((cur_start, cur_end))
                cur_start, cur_end = start, end
            else:
                cur_end = max(cur_end, end)
        merged.append((cur_start, cur_end))

        max_gap = max(merged[0][0] - px1, px2 - merged[-1][1])
        for i in range(1, len(merged)):
            max_gap = max(max_gap, merged[i][0] - merged[i - 1][1])

        ans = max_gap

    if ans <= 0:
        print("No View")
    else:
        print(round(Decimal(float(ans)), 2))
