import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
print(' ' * (N - 1) + '*')
for i in range(2, N + 1):
    print(' ' * (N - i) + '*' + ' ' * (2 * i - 3) + '*')
