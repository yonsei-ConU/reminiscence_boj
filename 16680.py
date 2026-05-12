import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def digit_sum(n):
    return sum(map(int, str(n)))


for _ in range(int(input_())):
    N = int(input_())
    for mul in [99999999, 999999999]:
        if digit_sum(N * mul) & 1:
            print(N * mul)
            break
    else:
        print(-1)
