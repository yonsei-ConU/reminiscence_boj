import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans = 0

while N != 1:
    ans += 1
    if N & 1:
        N = 3 * N + 1
    else:
        N >>= 1

print(ans)
