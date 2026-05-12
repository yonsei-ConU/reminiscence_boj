import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
A = list(minput())
diff = sorted([A[i + 1] - A[i] for i in range(N - 1)])
print(sum(diff[:N - K]))
