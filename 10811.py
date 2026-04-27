import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
ans = [i + 1 for i in range(N)]
for _ in range(M):
    i, j = minput()
    i -= 1
    ans[i:j] = ans[i:j][::-1]

print(*ans)
