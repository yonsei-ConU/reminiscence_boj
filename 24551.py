import sys
from math import lcm
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
num = [int('1' * v) for v in range(2, 19)]
ans = 0
for mask in range(1 << len(num)):
    cur = 1
    for i in range(len(num)):
        if mask & (1 << i):
            cur = lcm(cur, num[i])
    ans += (-1) ** mask.bit_count() * (N // cur)

print(N - ans)
