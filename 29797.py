import sys
from collections import Counter
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    P = int(input_())
    S = list(input_().split())
    last = ''.join(sorted(S[0]))
    ans = [last]

    for i in range(1, P + 1):
        cnt = Counter(S[i])
        distinct = set(S[i])

        j = 0
        while j < len(last):
            for c in sorted(distinct):
                if c < last[j]: continue
                """Flag 9m 43s"""
