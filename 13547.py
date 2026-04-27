import sys
from math import isqrt
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())
def make_key(x): s, e, _ = x; return (s // rN, e)


def process(idx, operation):
    global ans
    if operation:
        if not count[A[idx]]:
            count[A[idx]] = 1
            ans += 1
        else:
            count[A[idx]] += 1
    else:
        count[A[idx]] -= 1
        if not count[A[idx]]:
            ans -= 1


N = int(input_())
A = list(minput())
M = int(input_())
queries = [list(minput()) + [i] for i in range(M)]
answers = [None] * M
rN = isqrt(N)
queries.sort(key=make_key)
count = {}
for a in A: count[a] = 0
ans = 0
last_s = -1
last_e = -1
for s, e, q in queries:
    if last_s == -1:
        for idx in range(s, e + 1):
            process(idx, 1)
    else:
        while last_s < s:
            process(last_s, 0)
            last_s += 1
        while last_s > s:
            last_s -= 1
            process(last_s, 1)
        while last_e < e:
            last_e += 1
            process(last_e, 1)
        while last_e > e:
            process(last_e, 0)
            last_e -= 1
    last_s, last_e = s, e
    answers[q] = ans

print(*answers, sep="\n")
