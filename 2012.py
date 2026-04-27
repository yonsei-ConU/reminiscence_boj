import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = sorted([int(input_()) for _ in range(N)])
print(sum(abs(A[i] - i - 1) for i in range(N)))
