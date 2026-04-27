import sys
from itertools import permutations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
for p in permutations(list(range(1, N + 1))):
    diff = [abs(p[i + 1] - p[i]) for i in range(len(p) - 1)]
    if max(diff) > 2 or p[0] != 1:
        continue
    last = diff[0]
    chk = True
    for cur in diff[1:]:
        if last * 2 == cur or cur * 2 == last:
            last = cur
            continue
        chk = False
        break
    if chk:
        print(*p)
    
