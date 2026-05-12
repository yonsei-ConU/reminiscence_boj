import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
B = list(minput())
gifts = defaultdict(list)
for i in range(N):
    gifts[B[i]].append(A[i])

ans = 0
last = 0
for key in sorted(gifts):
    new_last = 0
    for time in gifts[key]:
        # last이상 time이상이고 time과 합동 (mod30) 인 가장 작은 x
        x = time % 30
        t1 = key // 30 * 30 + x
        if t1 < key:
            t1 += 30
        t2 = last // 30 * 30 + x
        if t2 < last:
            t2 += 30
        t = max(t1, t2)
        a, b = divmod(t - time, 30)
        assert not b
        if a < 0:
            t -= a * 30
            a = 0
        ans += a
        new_last = max(new_last, t)
    last = new_last

print(ans)
