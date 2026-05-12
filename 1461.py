import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
books = deque(sorted(minput()))
ans = 0
lst = []
while N:
    m = 0
    tmp = 0
    while N and m < M and books[0] < 0:
        N -= 1
        m += 1
        tmp = min(tmp, books.popleft())
    lst.append(-tmp)
    tmp = 0
    m = 0
    while N and m < M and books[-1] > 0:
        N -= 1
        m += 1
        tmp = max(tmp, books.pop())
    lst.append(tmp)

print(2 * sum(lst) - max(lst))
