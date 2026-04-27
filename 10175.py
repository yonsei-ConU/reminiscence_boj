import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    name, cnt = input_().split()
    C = cnt.count('C')
    B = cnt.count('B') * 2
    W = cnt.count('W') * 3
    M = cnt.count('M') * 4
    lst = [C, B, W, M]
    m = max(lst)
    if lst.count(m) != 1:
        ans = 'There is no dominant species'
    else:
        if m == C:
            t = 'Coyote'
        elif m == B:
            t = 'Bobcat'
        elif m == W:
            t = 'Wolf'
        else:
            t = 'Mountain Lion'
        ans = f'The {t} is the dominant species'
    print(f'{name}: {ans}')
