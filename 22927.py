import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for abc in range(1, int(input_()) + 1):
    S = input_().rstrip()
    T = input_().rstrip()
    cnt = S.count('0') + S.count('?') - T.count('0')
    if cnt < 0:
        print(f'Case {abc}: -1')
    else:
        onezero = 0
        zeroone = 0
        qzero = 0
        qone = 0
        for i in range(len(S)):
            if S[i] == '0' and T[i] == '1':
                zeroone += 1
            elif S[i] == '1' and T[i] == '0':
                onezero += 1
            elif S[i] == '?':
                if T[i] == '0':
                    qzero += 1
                else:
                    qone += 1
        ans = 0
        ans += qone + qzero
        t = min(zeroone, onezero)
        zeroone -= t
        onezero -= t
        ans += t
        ans += onezero + zeroone
        print(f'Case {abc}: {ans}')
