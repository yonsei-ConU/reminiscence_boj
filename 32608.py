import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def v(s): return 10 ** 1.5 * s ** (1/6)


n, h = minput()
droplets = [list(minput()) for _ in range(n)]
droplets.append([0, h])
ans = 0
size, cur_y = droplets[0]

for s, y in droplets[1:]:
    ans += (y - cur_y) / v(size)
    size += s
    cur_y = y

print(ans)
