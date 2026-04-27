import sys
from random import shuffle
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


print(6)
M = 125
multiples = [M]
while multiples[-1] < 1000000:
    multiples.append(multiples[-1] + M)

multiples = [m for m in multiples if 100000 <= m < 1000000]
decimal = {}
for m in multiples:
    n = m
    tmp = []
    while m:
        tmp.append(m % 10)
        m //= 10
    decimal[n] = (tmp[::-1])

delim = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cur = 110000
for i in range(len(multiples)):
    if multiples[i - 1] < cur and multiples[i] >= cur:
        delim.append(i)
        cur += 10000

delim.append(len(multiples))

for i in [936125]:
    if '0' in str(i):
        continue
    for j in [271000]:
        if i == j:
            continue
        ans = [i, j, 0, 0, 0, 0]
        s = {i, j}
        chk = True
        for k in range(6):
            start = decimal[i][k] * 10 + decimal[j][k]
            lst = multiples[delim[start]:delim[start + 1]]
            shuffle(lst)
            for v in lst:
                if v not in s:
                    print(v)
                    s.add(v)
                    asdf = str(v)
                    for z in range(2, 6):
                        ans[z] += int(asdf[z]) * 10 ** (5 - k)
                    break
            else:
                chk = False
                break
        if not chk:
            continue
        print(ans)
        diagonal1 = (ans[0] // 100000) * 100000 + ((ans[1] % 100000) // 10000) * 10000 + ((ans[2] % 10000) // 1000) * 1000 + ((ans[3] % 1000) // 100) * 100 + ((ans[4] % 100) // 10) * 10 + ans[5] % 10
        diagonal2 = ans[5] // 100000 + (ans[4] % 100000) // 10000 + (ans[3] % 10000) // 1000 + (ans[2] % 1000) // 100 + (ans[1] % 100) // 10 + ans[0] % 10
        print(diagonal1, diagonal2)
        if not diagonal1 % M and not diagonal2 % M and diagonal1 not in ans and diagonal2 not in ans:
            for a in ans:
                print(*a)
