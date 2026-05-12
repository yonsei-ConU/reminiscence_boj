import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


X = list(input_().rstrip())
N = len(X)
cnt1 = 0
ksa = 'KSA'
for x in X:
    if x == ksa[cnt1 % 3]:
        cnt1 += 1

Y = ['K'] + X
cnt2 = 0
for x in Y:
    if x == ksa[cnt2 % 3]:
        cnt2 += 1

Z = ['K', 'S'] + X
cnt3 = 0
for x in Z:
    if x == ksa[cnt3 % 3]:
        cnt3 += 1

m = max(cnt1, cnt2, cnt3)
if m == cnt1:
    print((N - cnt1) << 1)
elif m == cnt2:
    print((N + 1 - min(N, cnt2)) << 1)
else:
    print((N + 2 - min(N, cnt3)) << 1)
