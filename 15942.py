import sys
from heapq import heappush
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
k, p = minput()
l = []
q = p
while q:
    l.append(q)
    q >>= 1

if len(l) > k:
    exit(print(-1))

l = l[::-1]
ans = [''] * N
l_ptr = 0
r_ptr = len(l) + (len(l) == k)
for i in range(1, N + 1):
    if i == p:
        ans[i - 1] = str(k)
    elif i == l[l_ptr]:
        l_ptr += 1
        ans[i - 1] = str(l_ptr)
    else:
        ans[i - 1] = str(r_ptr)
        r_ptr += 1
        if r_ptr == k:
            r_ptr += 1

heap = []
for i in ans:
    i = int(i)
    heappush(heap, i)

if ans == list(map(str, heap)):
    print('\n'.join(ans))
else:
    print(-1)
