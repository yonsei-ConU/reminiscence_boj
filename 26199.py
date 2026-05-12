import sys
from algorithms import segtree, permutation_cycle_decomposition
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


n = int(input_())
inv = list(minput())
st = segtree([1] * n, add, 0)
perm = [0] * n
for i in range(n):
    x = inv[i]
    lo = -1
    hi = n
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if st.query(0, mid) > x:
            hi = mid
        else:
            lo = mid
    perm[hi] = i + 1
    st.update(hi, 0)

cycles = permutation_cycle_decomposition(n, perm)
ans = []
for cycle in cycles:
    cycle = ' '.join(map(str, cycle))
    ans.append(f"({cycle})")

print(' '.join(ans))
