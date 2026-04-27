import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


G = int(input_())
K, L = minput()
for _ in range(G):
    N = int(input_())
    input_()
    M = int(input_())
    input_()
    if K == 1 or N == M:
        print("YS")
    elif N < M:
        print("Y")
    else:
        print("S")
