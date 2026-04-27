import sys
from math import isqrt
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())


def mos(seq, queries):
    def make_key(x): s, e, _ = x; return (s // rL, e)


    def process(idx, operation):
        """
        modify this function only
        according to problem query
        operation = 1 then add
        operation = 0 then delete
        """
        nonlocal ans
        if operation:
            if count[seq[idx]] == ans:
                ans += 1
            count[seq[idx]] += 1
            count_rev[count[seq[idx]]] += 1
            count_rev[count[seq[idx]] - 1] -= 1
        else:
            count[seq[idx]] -= 1
            count_rev[count[seq[idx]]] += 1
            count_rev[count[seq[idx]] + 1] -= 1
            if not count_rev[count[seq[idx]] + 1]:
                ans -= 1


    ans = 0
    L = len(seq)
    rL = isqrt(L)
    Q = len(queries)
    answers = [None] * Q
    queries.sort(key=make_key)
    count = {}
    for a in A: count[a] = 0
    count_rev = [0] * L
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
        answers[q] = str(ans)
    return answers


N = int(input_())
A = list(minput())
M = int(input_())
queries = [list(minput()) + [i] for i in range(M)]
answers = mos(A, queries)
for a in answers:
    sys.stdout.write(a + '\n')
