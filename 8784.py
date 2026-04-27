import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    N = int(input_())
    S = list(minput())
    p = [0] * N
    a = [0] * N
    check = True
    for i in range(N >> 1):
        left, right = S[i], S[N - 1 - i]
        if (left + right) % 2:
            check = False
            break
        p_next = (left + right) // 2
        p[i] = p_next
        p[N - 1 - i] = p_next
        a_next = (right - left) // 2
        a[N - 1 - i] = a_next
        a[i] = -a_next
    if not check:
        print('NIE')
    else:
        print(' '.join(map(str, p)))
        print(' '.join(map(str, a)))
