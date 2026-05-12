import sys
from bisect import bisect_right as upper_bound
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


pre = [111, 117, 119, 171, 231, 237, 297, 319, 371, 411, 413, 417, 437, 471, 473, 531, 537, 597, 611, 671, 679, 711, 713, 717, 731, 737, 831, 837, 897, 973, 979, 1131, 1137, 1311, 1313, 1317, 1379, 1797, 1971, 3113, 3131, 3173, 3179, 4197, 4311, 4313, 4317, 4797, 6137, 6179, 7197, 7971, 31373]
for _ in range(int(input_())):
    N = int(input_())
    idx = upper_bound(pre, N) - 1
    print(-1 if idx == -1 else pre[idx])
