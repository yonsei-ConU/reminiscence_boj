import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    N, K = minput()
    asdf = K
    res = []
    while K:
        k = str(K)
        x = int(k[0] * len(k))
        if K < x:
            x -= int('1' * len(k))
            if x <= 0:
                x = int('9' * (len(k) - 1))
        K -= x
        res.append(x)
    print(len(res))
    print(*res)
