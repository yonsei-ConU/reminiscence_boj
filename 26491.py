import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def ps(i):
    if i == -1:
        return 0
    return ps_[i]


n, S = minput()
a = sorted(list(minput()))
ps_ = []
cur_sum = 0
for i in range(n):
    cur_sum += a[i]
    ps_.append(cur_sum)

start = 0
end = 1
s = a[end] - a[start]
if s > S or n == 1: exit(print(1))
ans = 2

while end < n:
    if s > S:
        s -= ps(end) - ps(start) - a[start] * (end - start)
        start += 1
        ans = max(ans, end - start + 1)
    else:
        ans = max(ans, end - start + 1)
        end += 1
        if end == n: break
        s += a[end] * (end - start) - ps(end - 1) + ps(start - 1)

print(ans)
