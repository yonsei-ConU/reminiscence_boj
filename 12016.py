import sys
from algorithms import segtree
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


N = int(input_())
times = list(minput())
queries = []
for i in range(N):
    queries.append((times[i], i))

queries.sort()
st = segtree([1] * N, add, 0)
last_val = 0
last_idx = N
time = 0
output = [''] * N
for v, idx in queries:
    if v > last_val:
        time += st.query(last_idx, N - 1)
        time += (v - 1 - last_val) * st.query(0, N - 1)
        time += st.query(0, idx)
    elif v == last_val:
        time += st.query(last_idx, idx)
    output[idx] = str(time)
    last_val = v
    last_idx = idx
    st.update(idx, 0)

print('\n'.join(output))
