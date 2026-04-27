import sys
input_ = sys.stdin.readline
def print_(*args)       : print(*args, flush=True)
def minput(): return map(int, input_().split())
def find_digit_sum(x):return sum(int(c) for c in str(x))


print_('query 0')
digit_sum = int(input_())

expo = 0
ans = [0] * 18
while expo < 18:
    lo = 0
    hi = 10
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        print_('query', mid * (10 ** expo))
        t = int(input_())
        if t < digit_sum + find_digit_sum(mid * (10 ** expo)):
            hi = mid
        else:
            lo = mid
    ans[expo] = lo
    expo += 1

print('answer', 10 ** 18 - 1 - sum(ans[i] * 10 ** i for i in range(18)))
