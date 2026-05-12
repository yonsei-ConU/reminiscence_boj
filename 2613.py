import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
rntmf = list(minput())

lo = max(rntmf) - 1
hi = sum(rntmf) + 1

while lo + 1 < hi:
    mid = (lo + hi) >> 1
    group_count = 1
    cur_sum = 0

    for num in rntmf:
        if cur_sum + num > mid:
            group_count += 1
            cur_sum = num
        else:
            cur_sum += num

    if group_count > M:
        lo = mid
    else:
        hi = mid

print(hi)

ans = []
cur_sum = 0
temp = 0
for i in range(N):
    if cur_sum + rntmf[i] > hi or (N + 1 - i) == M - len(ans):
        ans.append(temp)
        temp = 1
        cur_sum = rntmf[i]
    else:
        cur_sum += rntmf[i]
        temp += 1

ans.append(temp)
print(*ans)
