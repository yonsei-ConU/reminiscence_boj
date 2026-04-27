import sys
from bisect import bisect_right as upper_bound
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


fib = [1, 2]
while fib[-1] < 10 ** 18:
    fib.append(fib[-1] + fib[-2])

N = int(input_())
ans = []
while N:
    idx = upper_bound(fib, N) - 1
    ans.append(fib[idx])
    N -= fib[idx]

print(len(ans))
print(*ans[::-1])
