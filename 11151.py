import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    N = int(input_())
    W, C, F = minput()
    cities = [list(minput()) for _ in range(N)]
    ans = 20
    for mask in range(1, 1 << N):
        w = c = f = 0
        for i in range(N):
            if mask & (1 << i):
                w += cities[i][0]
                c += cities[i][1]
                f += cities[i][2]
        if w >= W and c >= C and f >= F:
            ans = min(ans, mask.bit_count())
    print(ans if ans != 20 else 'game over')
