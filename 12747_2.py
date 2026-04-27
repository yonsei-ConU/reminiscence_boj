from collections import deque
n, k = map(int, input().split())
ans = set()
for mask in range(k ** n):
    lst = deque()
    m = mask
    for i in range(n):
        lst.append(m % k)
        m //= k
    ...
