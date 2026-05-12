import sys
from algorithms import segtree, sieve
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def mult(a, b): return a * b % MOD


primes = sieve(1299709)
MOD = 584039225158817291
for _ in range(int(input_())):
    N, K = minput()
    st = segtree(primes, mult, 1)
    st_original = segtree(primes, mult, 1)

    for i in range(K):
        Q, A, B = minput()
        if not Q:
            curA = st.query(A, A)
            curB = st.query(B, B)
            st.update(A, curB)
            st.update(B, curA)
        else:
            t1 = st.query(A, B)
            t2 = st_original.query(A, B)
            print('YNEOS'[t1 != t2::2])
