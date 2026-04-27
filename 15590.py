import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, R = minput()
c = sorted([int(input_()) for _ in range(N)])
stores = sorted([tuple(minput()) for _ in range(M)], key=lambda x: -x[1])
neighbors = sorted([int(input_()) for _ in range(R)], reverse=True)

