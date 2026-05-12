import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
for tc in range(1, N + 1):
    R, C = minput()
    mat = [list(minput()) for _ in range(R)]
    p = [0, 0]
    m = [0, 0]
    for y in range(R):
        for x in range(C):
            val = mat[y][x]
            p[(y + x) & 1] += val
            m[(y - x) % 2] += val
    if p[0] == p[1] and m[0] == m[1]:
        ans = "YES"
    else:
        ans = "NO"
    print(f"Case #{tc}: {ans}")
    if tc ^ N:
        print()
