import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, K = minput()
A = sorted(list(minput()) + [0])
dist = []
for i in range(N):
    dist.append(abs(A[i + 1] - A[i]))
dist.sort(reverse=True)
print(sum(dist[K:]))
