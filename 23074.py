import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans = []
for i in range(1, N + 1):
    if i & 1:
        ans.append((i + 1) >> 1)
    else:
        ans.append(i >> 1)

if N & 1:
    ans[-1] = 1
print(N >> 1 if N != 1 else 1)
print(*ans)
