import sys
from random import randint
from algorithms import segtree, sieve
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def mult(a, b): return a * b % MOD


primes = sieve(29)
MOD = 998244353


def right(data):
    st = segtree(primes, mult, 1)
    st_original = segtree(primes, mult, 1)
    ret = []

    for Q, A, B in data:
        if not Q:
            curA = st.query(A, A)
            curB = st.query(B, B)
            st.update(A, curB)
            st.update(B, curA)
        else:
            t1 = st.query(A, B)
            t2 = st_original.query(A, B)
            ret.append('YNEOS'[t1 != t2::2])

    return ret


def wrong(data, N):
    st = segtree(list(range(1, N + 1)), mult, 1)
    st_original = segtree(list(range(1, N + 1)), mult, 1)
    ret = []

    for Q, A, B in data:
        if not Q:
            curA = st.query(A, A)
            curB = st.query(B, B)
            st.update(A, curB)
            st.update(B, curA)
        else:
            t1 = st.query(A, B)
            t2 = st_original.query(A, B)
            ret.append('YNEOS'[t1 != t2::2])

    return ret


def generate():
    N = randint(3, 6)
    K = randint(3, 6)
    data = []
    for i in range(K):
        a = randint(0, 1)
        b = randint(0, N - 2)
        c = randint(b + 1, N - 1)
        data.append([a, b, c])
    return N, data


for i in range(1, 10001):
    N, data = generate()
    r = right(data)
    w = wrong(data, N)
    bsn = '\n'
    if r != w:
        print(f"Test case #{i} failed")
        print(f"Input {N} {data}")
        print(f"Expected: {r}")
        print(f"Received: {w}")
        break
else:
    print(f"10000 Test case passed")
