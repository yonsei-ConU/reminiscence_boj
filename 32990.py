import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans = N * N // 4
print(ans)
if ans > 1000000:
    exit()
for diff in range(1, N):
    for start in range(1, diff + 1):
        if start + diff > N:
            break
        ans = []
        cur = start
        while cur + diff <= N:
            ans += [str(cur), str(cur + diff)]
            cur += diff
        print(len(ans) // 2, end=' ')
        print(' '.join(ans))
