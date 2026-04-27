import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


l, s = minput()
if l == 4:
    if s != 1:
        print(-1)
    else:
        print(4)
        print(0, 0)
        print(1, 0)
        print(1, 1)
        print(0, 1)
    exit()
if l & 1:
    exit(print(-1))

x = l >> 1
if x & 1:
    p = x >> 1
    q = p + 1
else:
    p = q = x >> 1

min_area = p + q - 1
max_area = p * q
if not min_area <= s <= max_area:
    exit(print(-1))

fill_area = s - min_area
filled, remainder = divmod(fill_area, q - 1)

ans = [(0, 0), (0, q), (1 + filled, q)]
if remainder:
    ans.append((1 + filled, 1 + remainder))
    ans.append((2 + filled, 1 + remainder))
    if 2 + filled != p:
        ans.append((2 + filled, 1))
else:
    if 1 + filled != p:
        ans.append((1 + filled, 1))

ans.append((p, 1))
ans.append((p, 0))

print(len(ans))
for x, y in ans:
    print(x, y)
