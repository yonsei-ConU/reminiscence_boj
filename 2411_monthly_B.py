import sys
from algorithms import segtree
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def add(a, b): return a + b


MOD = 10 ** 9 + 7
N, Q = minput()
A = list(minput())
st = segtree(A, add, 0)
w = [t * (t - 1) for t in A]
diff = [0] * N

for _ in range(Q):
    l, r = minput()
    total = st.query(l - 1, r - 1)
    d = pow(total, -1, MOD)
    diff[l - 1] = (diff[l - 1] + d) % MOD
    if r != N:
        diff[r] = (diff[r] - d) % MOD

real = [0] * N
for i in range(N):
    real[i] = (real[i - 1] + diff[i]) % MOD

ans = [(w[i] * real[i]) % MOD for i in range(N)]
print(*ans)
