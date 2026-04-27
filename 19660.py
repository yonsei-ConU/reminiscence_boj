import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
if n <= 5:
    print(-1)
else:
    res = [0] * n
    res[0] = res[1] = res[3] = 1
    print(*res)
