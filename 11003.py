import sys
from algorithms import segtree
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, L = minput()
st = segtree(list(minput()), min, 1e9)
d = [st.query(max(0, i - L + 1), i) for i in range(N)]
print(*d)
