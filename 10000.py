import sys
from algorithms import UnionFind
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def bit_and(a, b): return a & b


def coordinate_compression(lst):
    distinct = sorted(set(lst))
    rank = {distinct[i]: i for i in range(len(distinct))}
    return rank


N = int(input_())
circles_input = []
for _ in range(N):
    x, r = minput()
    circles_input.append([r, x])
circles_input.sort()

circles_raw = []
coordinates_raw = []
for r, x in circles_input:
    p, q = x - r, x + r
    coordinates_raw.extend([p, q])
    circles_raw.append([p, q])

rank = coordinate_compression(coordinates_raw)
circles = []
M = 0
for p, q in circles_raw:
    x, y = rank[p] * 2 + 1, rank[q] * 2 + 1
    circles.append([x, y])
    M = max(M, x, y)

set_bit = [0] * (M + 1)
uf = UnionFind(M + 1)
ans = 1
for l, r in circles:
    ans += 1 + (uf.find(l) == uf.find(r - 1))
    if set_bit[l - 1]:
        uf.union(l - 1, l)
    if set_bit[r]:
        uf.union(r - 1, r)
    set_bit[l] = set_bit[r - 1] = 1
    uf.union(l, r - 1)

print(ans)
