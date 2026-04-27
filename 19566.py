import sys
from collections import Counter
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def nc2(n):
    return n * (n - 1) // 2


N, K = minput()
A = list(minput())
psum2 = [0]
for v in A:
    psum2.append(psum2[-1] + v - K)

cnt = Counter(psum2)
ans = 0
for v in cnt.values():
    ans += nc2(v)

print(ans)
