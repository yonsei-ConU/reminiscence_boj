import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if N % 2:
    print(N // 2)
else:
    print(N - 1)
