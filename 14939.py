import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def f(x):
    ret = 1 << x
    if x != 9:
        ret += 1 << (x + 1)
    if x:
        ret += 1 << (x - 1)
    return ret


ipt = [input_().rstrip() for _ in range(10)]
grid = []
for row in ipt:
    t = 0
    for i in range(10):
        if row[i] == 'O':
            t += 1 << i
    grid.append(t)

ans = 101
for mask in range(1024):
    new_grid = grid.copy()
    tmp = 0
    for i in range(10):
        if mask & (1 << i):
            new_grid[0] ^= f(i)
            new_grid[1] ^= (1 << i)
            tmp += 1

    for i in range(1, 10):
        for j in range(10):
            if new_grid[i - 1] & (1 << j):
                new_grid[i - 1] ^= 1 << j
                new_grid[i] ^= f(j)
                if i != 9:
                    new_grid[i + 1] ^= 1 << j
                tmp += 1

    if not sum(new_grid):
        ans = min(ans, tmp)

assert ans != -1
print(ans)
