import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
if K > N * 25 + 1: exit(print(-1))
S = list(input_().strip())
alph = [ord(i) - 65 for i in S]
ps = []
cur_sum = 0
for i in range(N):
    cur_sum += alph[i]
    ps.append(cur_sum)

cur_sum += 1
ps.append(cur_sum)
for i in range(N)[::-1]:
    cur_sum += 25 - alph[i]
    ps.append(cur_sum)

lo = -1
hi = len(ps)
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if ps[mid] >= K:
        hi = mid
    else:
        lo = mid

if ps[N] > K:
    if not hi:
        S[0] = chr(K + 64)
    else:
        S[hi] = chr(K - ps[hi - 1] + 64)
elif ps[N] < K:
    idx = 2 * N - hi
    S[idx] = chr(alph[idx] + K - ps[hi - 1] + 65)
print(''.join(S))
