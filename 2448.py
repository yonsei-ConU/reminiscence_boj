import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def star(cur, n, start):
    y, x = start
    if n == 3:
        dy = [0,  1, 1,  2,  2, 2, 2, 2]
        dx = [0, -1, 1, -2, -1, 0, 1, 2]
        for i in range(8):
            cur[y + dy[i]][x + dx[i]] = '*'
    else:
        cur = star(cur, n // 2, start)
        cur = star(cur, n // 2, (y + n//2, x - n//2))
        cur = star(cur, n // 2, (y + n//2, x + n//2))
    return cur


N = int(input_())
ans = star([[' '] * (2 * N - 1) for _ in range(N)], N, (0, N - 1))
for a in ans:
    print(''.join(a))
