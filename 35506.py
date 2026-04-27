import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
cnt = N
for i in range(2 * N):
    print((2 * N - i - 1) * ' ' + '*', end='')
    if i == N: cnt += 1
    if i > N: cnt += 2
    print(" " * cnt + '*', end='')
    print(" " * min(2 * i + 1, 2 * (2 * N - i - 1) + 1) + '*', end='')
    if i < N:
        print(" " * (N - 1 - i))
    else:
        print(" " * (i - N))
