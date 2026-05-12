from random import randint
from math import acos
from tqdm import trange
from algorithms import *

MAX_TC = 1000000

def mult(a, b): return a * b % MOD
primes = sieve(29)
MOD = 998244353

def naive(data):
    st = segtree(primes, mult, 1)
    st_original = segtree(primes, mult, 1)
    ret = []

    for Q, A, B in data[1]:
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


def solve(data):
    N = data[0]
    st = segtree(list(range(1, N + 1)), mult, 1)
    st_original = segtree(list(range(1, N + 1)), mult, 1)
    ret = []

    for Q, A, B in data[1]:
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


def generator():
    N = randint(3, 6)
    K = randint(3, 6)
    data = []
    for i in range(K):
        a = randint(0, 1)
        b = randint(0, N - 2)
        c = randint(b + 1, N - 1)
        data.append([a, b, c])
    return N, data


def check(data, naive_sol, sol):
    return naive_sol == sol


try:
    for tc in trange(MAX_TC, desc="Running tests", unit="case"):
        data = generator()
        naive_solution = naive(data)
        solution = solve(data)
        if not check(data, naive_solution, solution):
            print(f"\nTest case #{tc + 1} failed")
            print(f"Input: {data}")
            print(f"Expected: {naive_solution}")
            print(f"Received: {solution}")
            break
    else:
        print(f"\n{MAX_TC} test cases passed")
except KeyboardInterrupt:
    print(f"\nStopping. Currently {tc} Test cases passed")
    print(f"Last Input: {data}")
