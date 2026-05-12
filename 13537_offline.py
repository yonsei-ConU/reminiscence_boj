import sys
from collections import defaultdict
from algorithms import segtree
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


N = int(input_())
A = list(minput())
A_rev = defaultdict(list)
for i in range(N):
    A_rev[A[i]].append(i)
A_rev[0] = []
M = int(input_())
output = [''] * M
queries = []
for idx in range(M):
    i, j, k = minput()
    queries.append((k, i, j, idx))

queries.sort(reverse=True)
qptr = 0
st = segtree([0] * N, add, 0)

for value in sorted(A_rev.keys(), reverse=True):
    while qptr < len(queries) and queries[qptr][0] >= value:
        ans = st.query(queries[qptr][1] - 1, queries[qptr][2] - 1)
        output[queries[qptr][3]] = str(ans)
        qptr += 1
    for idx in A_rev[value]:
        st.update(idx, 1)

print('\n'.join(output))
