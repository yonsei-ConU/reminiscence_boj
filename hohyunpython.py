import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
assert 1 <= N <= 500

print(N * (N - 1) // 2 + (N // 2 - 1) * (N & 1 ^ 1))
