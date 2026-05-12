import sys
from algorithms import segtree
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


n, q = minput()
st = segtree([0] * 2 * n, add, 0)

for _ in range(q):
    query = input_().split()
    if query[0] == '-':
        a = int(query[1]) - 1
        st.update(a, 1)
        st.update(a + n, 1)
    elif len(query) == 2:
        a = int(query[1]) - 1
        st.update(a, 0)
        st.update(a + n, 0)
    else:
        a, b = map(lambda x: int(x) - 1, query[1:])
        if a < b:
            s = min(st.query(a, b), st.query(b, a + n))
        else:
            s = min(st.query(b, a), st.query(a, b + n))
        if not s:
            print('possible')
        else:
            print('impossible')
