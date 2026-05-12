import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while 1:
    N, M, Q = minput()
    if not N: break

    switch = [(1 << N) - 1] * M
    totalS = 0
    for _ in range(Q):
        S, B = input_().split()
        newS = int(S[::-1], 2)
        totalS ^= newS
        for i in range(M):
            if B[i] == '1':
                switch[i] &= totalS

    ans = ['?'] * M
    prev = [''] * M
    while '?' in ans:
        if 0 in switch:
            assert False
        if ans == prev: break
        prev = ans[:]
        tmp = []
        for i in range(M):
            if ans[i] != '?': continue
            x = switch[i]
            if bin(x).count('1') == 1:
                one = bin(x).find('1')
                t = len(bin(x)) - one - 1
                if t < 10:
                    ans[i] = str(t)
                else:
                    ans[i] = chr(55 + t)
                tmp.append(t)
        for t in tmp:
            switch = list(map(lambda z: z & (((1 << N) - 1) ^ (1 << t)), switch))

    print(''.join(ans))

# 1:41:00
