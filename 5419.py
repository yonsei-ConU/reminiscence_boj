import sys
from algorithms import segtree
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


for _ in range(int(input_())):
    n = int(input_())
    y = set()
    islands = []
    for i in range(n):
        xi, yi = minput()
        y.add(yi)
        islands.append((xi, yi))
    islands.sort(key=lambda x: (-x[0], x[1]))
    distinct = sorted(set(y))
    rank = {distinct[i]: i for i in range(len(distinct))}
    st = segtree([0] * len(distinct), add, 0)
    ans = 0
    for x, y in islands:
        ans += st.query(0, rank[y])
        st.update(rank[y], st.tree[st.n + rank[y]] + 1)
    print(ans)
