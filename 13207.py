import sys

input_ = sys.stdin.readline
t = int(input_())


def get_line(p1, p2):
    if p1[0] == p2[0]:
        return (None, p1[0], True)
    else:
        inclination = (p1[1] - p2[1]) / (p1[0] - p2[0])
        ywjfvus = p1[1] - p1[0] * inclination
        return (inclination, ywjfvus, False)


def line_substitute(line, x):
    if line[2]:
        return None
    else:
        return line[0] * x + line[1]


def inverse_substitute(line, x):
    return 1 / line[0] * x - line[1] / line[0]


def dist(dot1, dot2):
    return (dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2


def area(x, y):
    r = 0
    for i in range(len(x)-1):
        r += x[i] * y[i+1]
    r += x[-1] * y[0]
    for i in range(len(y)):
        r -= x[i] * y[i-1]
    return abs(r) / 2


for _ in range(t):
    x0, y0, x1, y1 = map(int, input_().split())
    xa, ya, xb, yb, xc, yc = map(int, input_().split())
    A = (xa, ya)
    B = (xb, yb)
    C = (xc, yc)
    ccw = xa*yb + xb*yc + xc*ya - xb*ya - xc*yb - xa*yc
    if ccw < 0:
        B, C = C, B
    ab_line = get_line(A, B)
    bc_line = get_line(B, C)
    ca_line = get_line(C, A)
    A_side = [[] ,[]]
    B_side = [[], []]
    C_side = [[], []]

    f = line_substitute(ab_line, x0)
    if f is None:
        dot = (ab_line[1], y0, 0)
    else:

        if f < y0:
            dot = (inverse_substitute(ab_line, y0), y0, 0)
        elif y0 <= f <= y1:
            dot = (x0, f, 1)
        elif f > y1:
            dot = (inverse_substitute(ab_line, y1), y1, 2)
    if dist(dot, A) < dist(dot, B):
        A_side[1] = dot
    else:
        B_side[0] = dot


    f = line_substitute(ab_line, x1)
    if f is None:
        dot = (ab_line[1], y1, 2)
    else:
        if f < y0:
            dot = (inverse_substitute(ab_line, y0), y0, 0)
        elif y0 <= f <= y1:
            dot = (x1, f, 3)
        elif f > y1:
            dot = (inverse_substitute(ab_line, y1), y1, 2)
    if dist(dot, A) < dist(dot, B):
        A_side[1] = dot
    else:
        B_side[0] = dot

        
    f = line_substitute(bc_line, x0)
    if f is None:
        dot = (bc_line[1], y0, 0)
    else:
        if f < y0:
            dot = (inverse_substitute(bc_line, y0), y0, 0)
        elif y0 <= f <= y1:
            dot = (x0, f, 1)
        elif f > y1:
            dot = (inverse_substitute(bc_line, y1), y1, 2)
    if dist(dot, B) < dist(dot, C):
        B_side[1] = dot
    else:
        C_side[0] = dot

        
    f = line_substitute(bc_line, x1)
    if f is None:
        dot = (bc_line[1], y1, 2)
    else:
        if f < y0:
            dot = (inverse_substitute(bc_line, y0), y0, 0)
        elif y0 <= f <= y1:
            dot = (x1, f, 3)
        elif f > y1:
            dot = (inverse_substitute(bc_line, y1), y1, 2)
    if dist(dot, B) < dist(dot, C):
        B_side[1] = dot
    else:
        C_side[0] = dot

        
    f = line_substitute(ca_line, x0)
    if f is None:
        dot = (ca_line[1], y0, 0)
    else:
        if f < y0:
            dot = (inverse_substitute(ca_line, y0), y0, 0)
        elif y0 <= f <= y1:
            dot = (x0, f, 1)
        elif f > y1:
            dot = (inverse_substitute(ca_line, y1), y1, 2)
    if dist(dot, C) < dist(dot, A):
        C_side[1] = dot
    else:
        A_side[0] = dot

        
    f = line_substitute(ca_line, x1)
    if f is None:
        dot = (ca_line[1], y1, 2)
    else:
        if f < y0:
            dot = (inverse_substitute(ca_line, y0), y0, 0)
        elif y0 <= f <= y1:
            dot = (x1, f, 3)
        elif f > y1:
            dot = (inverse_substitute(ca_line, y1), y1, 2)
    if dist(dot, C) < dist(dot, A):
        C_side[1] = dot
    else:
        A_side[0] = dot
    
    ans = 0
    for side in (A_side, B_side, C_side):
        x_list = []
        y_list = []
        if side[0][2] == side[1][2]:
            if side == A_side:
                d = list(A)
            elif side == B_side:
                d = list(B)
            elif side == C_side:
                d = list(C)
            for dot in side + [d]:
                x_list.append(dot[0])
                y_list.append(dot[1])
        else:
            x_list.append(side[0][0])
            y_list.append(side[0][1])
            t = side[0][2]
            while t != side[1][2]:
                if t == 0:
                    x_list.append(x0)
                    y_list.append(x0)
                elif t == 1:
                    x_list.append(x0)
                    y_list.append(x1)
                elif t == 2:
                    x_list.append(x1)
                    y_list.append(y1)
                else:
                    x_list.append(x1)
                    y_list.append(y0)
                t = (t + 1) % 4
            x_list.append(side[1][0])
            if side == A_side:
                x_list.append(A[0])
            elif side == B_side:
                x_list.append(B[0])
            elif side == C_side:
                x_list.append(C[0])
            y_list.append(side[1][1])
            if side == A_side:
                y_list.append(A[1])
            elif side == B_side:
                y_list.append(B[1])
            elif side == C_side:
                y_list.append(C[1])
        ans += area(x_list, y_list)

    if ccw > 0:
        print(ans)
    else:
        print(abs(x1-x0) * abs(y1-y0) - ans)
