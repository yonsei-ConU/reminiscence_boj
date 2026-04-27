import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


cnt = defaultdict(int)
N = int(input_())
for v in list(minput()):
    cnt[v] += 1
ans = (N * N - N + 2) // 2
for v in cnt.values():
    ans -= v * (v - 1) // 2

print(ans)
