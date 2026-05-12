import sys
from itertools import permutations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
S = [list(minput()) for _ in range(N)]
ans = 10 ** 18
for mask in range(1 << N):
    if mask.bit_count() << 1 != N: continue
    start = []
    link = []
    for i in range(N):
        if mask & (1 << i):
            start.append(i)
        else:
            link.append(i)
    s = l = 0
    for p in permutations(start, 2):
        s += S[p[0]][p[1]]
    for p in permutations(link, 2):
        l += S[p[0]][p[1]]
    ans = min(ans, abs(s - l))

print(ans)
