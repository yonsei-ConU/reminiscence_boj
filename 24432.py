import sys
from itertools import combinations as combi
from math import comb
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n, m, k = minput()
    nCk = comb(n, k)
    mCk = comb(m, k)
    bob = list(minput())
    alice = list(minput())
    a_sum = sorted([sum(l) for l in combi(alice, k)])
    b_sum = sorted([sum(l) for l in combi(bob, k)])
    ans_max = max(abs(a_sum[0] - b_sum[-1]), abs(a_sum[-1] - b_sum[0]))
    a_ptr = 0
    b_ptr = 0
    ans_min = 10 ** 12
    while a_ptr < mCk and b_ptr < nCk:
        tmp = b_sum[b_ptr] - a_sum[a_ptr]
        ans_min = min(ans_min, abs(tmp))
        if tmp > 0:
            a_ptr += 1
        elif tmp < 0:
            b_ptr += 1
        else:
            break
    print(ans_min, ans_max)
