import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n = int(input_())
    points = [list(minput()) + [i] for i in range(1, 3 * n + 1)]
    points.sort()
    for i in range(0, 3 * n, 3):
        print(*[points[i + j][2] for j in range(3)])
