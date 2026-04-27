import sys
from collections import defaultdict
from bisect import bisect_left as bsl
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n, b = minput()
    tmp = defaultdict(list)
    hi = -1

    for i in range(n):
        type_, name, price, quality = input_().split()
        price = int(price)
        quality = int(quality)
        tmp[type_].append([quality, price])
        hi = max(hi, quality)

    qnvna = list(tmp.values())
    for i in range(len(qnvna)):
        qnvna[i].sort()
        suffix_min = 1000001
        for j in range(len(qnvna[i]))[::-1]:
            suffix_min = min(suffix_min, qnvna[i][j][1])
            qnvna[i][j][1] = suffix_min

    lo = -1
    hi += 1
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        price = 0
        valid = True
        for i in range(len(qnvna)):
            idx = bsl(qnvna[i], [mid, 0])
            if idx == len(qnvna[i]):
                valid = False
                break
            price += qnvna[i][idx][1]
        if not valid or price > b:
            hi = mid
        else:
            lo = mid

    print(lo)
