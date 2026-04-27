import sys
from math import gcd
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class UnionFind:
    def __init__(self, x):
        self.parent = [i for i in range(x)]
        self.size = [1] * x

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        elif self.size[root_x] >= self.size[root_y]:
            self.size[root_x] += self.size[root_y]
            self.parent[root_y] = root_x
        else:
            self.size[root_y] += self.size[root_x]
            self.parent[root_x] = root_y


N = int(input_())
lpf = [0, 0] + [1] * (999999)
prime_cnt = 0
for i in range(2, 1000001):
    if lpf[i] == 1:
        prime_cnt += 1
        for j in range(i, 1000001, i):
            lpf[j] = i

ID = list(minput())
fact = []
for v in ID:
    t = set()
    while v > 1:
        p = lpf[v]
        v //= p
        t.add(p)
    fact.append(t)

uf = UnionFind(1000001)
for s in fact:
    s = list(s)
    for i in range(1, len(s)):
        uf.union(s[0], s[i])

ans = defaultdict(int)
for v in ID:
    ans[uf.find(lpf[v])] += 1

print(max(ans.values()))
