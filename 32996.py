import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if N == 1:
    print(1)
    print("1 1 1 1")
else:
    print(2 * N - 1)
    print(1, N - 1, 1, 1)
    print(N, N + 1, N, 1)
    cur = N + 2
    for i in range(2, N):
        print(cur, cur + N - 1, i, 1)
        cur += N
        print(cur, cur, N, i + 1)
        cur += 1
    assert cur == N * N
    print(cur, cur, 1, N)
