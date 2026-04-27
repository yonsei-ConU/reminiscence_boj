import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, V = minput()
V -= 1
C = list(minput())
for _ in range(M):
    K = int(input_())
    if K < N:
        print(C[K])
    else:
        print(C[V + (K - V) % (N - V)])
