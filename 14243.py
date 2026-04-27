import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


S = input_().rstrip()
A = S.count('A')
B = S.count('B')
C = S.count('C')
if B <= A + 1:
    ans = ['' for _ in range(A + B)] 
    ans[0] = 'B'
    ptr = 1
    for i in range(B - 1):
        ans[ptr] = 'A'
        ans[ptr + 1] = 'B'
        ptr += 2
    for i in range(ptr, ptr + A + 1 - B):
        ans[i] = 'A'
    real_ans = ['' for _ in range(len(S))]
    c = C
    cur = 2
    ptr_ab = 0
    ptr = 0
    while c:
        if cur == 2:
            cur = 0
            real_ans[ptr] = 'C'
            c -= 1
        else:
            cur += 1
            if ptr_ab == A + B:
                exit(print(-1))
            real_ans[ptr] = ans[ptr_ab]
            ptr_ab += 1
        ptr += 1
    if ptr_ab != A + B:
        while ptr < A + B + C:
            real_ans[ptr] = ans[ptr_ab]
            ptr_ab += 1
            ptr += 1
    print(''.join(real_ans))
elif (B - 1) >> 1 < A:
    exit(print(-1))
elif B == 2 and C == 1:
    exit(print('BCB'))
else:
    c = B - 1 - A
    if C < c:
        exit(print(-1))
    ans = []
    c_left = C
    for i in range(B >> 1):
        ans += ['B', 'A', 'B', 'C']
        c_left -= 1
    if B & 1:
        ans += ['C', 'B']
        c_left -= 1
    assert c_left >= 0
    if not c_left:
        ...
    elif c_left == 1:
        ans = ['C'] + ans
    else:
        exit(print(-1))
    print(''.join(ans))
