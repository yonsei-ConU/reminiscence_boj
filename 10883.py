import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def merge(d1, d2, d3, d4):
    k = [set(d1.keys()), set(d2.keys()), set(d3.keys()), set(d4.keys())]
    k.sort(key=len, reverse=True)
    k[0] |= k[3]
    k[0] |= k[2]
    k[0] |= k[1]
    ret = {}
    for x in k[0]:
        ret[x] = (d1.get(x, 0) + d2.get(x, 0) + d3.get(x, 0) + d4.get(x, 0)) % MOD
    return ret


def dp_(x, y):
    if y > x: x, y = y, x
    if y == 1:
        dp[(x, y)] = {x: 1}
    elif (x, y) in dp:
        pass
    else:
        dp[(x, y)] = merge(dp_(x >> 1, y >> 1), dp_((x + 1) >> 1, y >> 1), dp_(x >> 1, (y + 1) >> 1), dp_((x + 1) >> 1, (y + 1) >> 1))
    return dp[(x, y)]


dp = {}
MOD = 1234567891
for _ in range(int(input_())):
    new_dp = {}
    for i in range(1, 17):
        for j in range(1, 17):
            if (i, j) in dp:
                new_dp[(i, j)] = dp[(i, j)]
    dp, new_dp = new_dp, dp
    N, M = minput()
    res = dp_(N, M)
    print(len(res))
    for k in sorted(res):
        print(k, res[k])
