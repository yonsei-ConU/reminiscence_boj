import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
tile_count = defaultdict(int)
for _ in range(n):
    a, b = minput()
    tile_count[a] += 1
    tile_count[b] += 1

ans = []
for x in tile_count:
    if tile_count[x] % 2:
        ans.append(x)

if len(ans) == 2:
    print(*sorted(ans))
elif not ans:
    if len(tile_count) == 1:
        a = list(tile_count.keys())[0]
        print(a, a)
    else:
        print('NIE')
else:
    print('NIE')
