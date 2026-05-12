# 9m 15.90s

import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


dy = [1, 1, 0, -1, -1]
dx = [0, 1, 1,  1,  0]
N = int(input_())
Q = list(map(lambda x: int(x) - 1, input_().split()))
available = [[1] * N for _ in range(N)]
