import sys
from collections import Counter
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
M = int(input_())
entry = list(minput())
exit_ = list(minput())
d = [exit_[j] - entry[i] for i in range(N) for j in range(M) if exit_[j] - entry[i] >= 0]
d = Counter(d)
ans_count = max(d.values())
for x in sorted(d.keys()):
    if d[x] == ans_count:
        print(x)
        break
