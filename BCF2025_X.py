import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
cnt = [0] * 10000
for i in range(N):
    for v in minput():
        cnt[v - 1] += 1

if not M & 1:
    bitor = 0
    for v in cnt:
        bitor |= v
    if bitor & 1:
        print("NO")
    else:
        print("YES")
else:
    odd_count = 0
    for v in cnt:
        if v & 1:
            odd_count += 1
    N -= odd_count
    if N < 0 or N & 1:
        print("NO")
    else:
        print("YES")
