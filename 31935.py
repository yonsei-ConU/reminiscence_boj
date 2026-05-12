import sys
from algorithms import segtree
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


N, K = minput()
A = list(minput())
lst = list(range(N))
lst.sort(key=lambda i: A[i])
lst = [i + 2 for i in lst]
st = segtree([0] * (N + 2), add, 0)
st.update(0, 1)
st.update(N + 1, 1)
for value in lst:
    st.update(value, 1)
    left = []
    right = []
    for i in range(K):
        ...
