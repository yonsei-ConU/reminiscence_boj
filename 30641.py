import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def f(i):
    if i >= 2:
        return pow(26, (i - 1) >> 1, 10 ** 9 + 7), pow(26, (i - 1) >> 1, 2)
    else:
        return 1, 1


L, U = minput()
ans = 0
ansmod2 = 0
for i in range(L, U + 1):
    a, b = f(i)
    ans = (ans + a) % (10 ** 9 + 7)
    ansmod2 = (ansmod2 + b) & 1

print('AH'[ansmod2 & 1])
print(ans)
