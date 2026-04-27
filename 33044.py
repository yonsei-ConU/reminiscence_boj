import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
cnt = [0] * 9
for value in A:
    cnt[value - 1] += 1


