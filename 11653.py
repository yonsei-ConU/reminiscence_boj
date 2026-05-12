import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def factorize(x):
    factor = 2
    ret = {}
    while x - 1:
        while x % factor:
            factor += 1
        if factor in ret:
            ret[factor] += 1
        else:
            ret[factor] = 1
        x //= factor
    return ret


N = int(input_())
factors = factorize(N)
for factor in sorted(factors):
    for i in range(factors[factor]):
        print(factor)
