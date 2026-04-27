import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
print(N * (N - 1))
