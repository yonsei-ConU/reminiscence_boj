import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
l = [int(input_()) for _ in range(n)]
plus = []
minus = []
zero = one = 0
for element in l:
    if element > 1:
        plus.append(element)
    elif element == 1:
        one += 1
    elif not element:
        zero += 1
    else:
        minus.append(element)

ans = 0
plus.sort()
minus.sort(reverse=True)
while len(minus) > 1:
    ans += minus.pop() * minus.pop()

if minus:
    m = minus.pop()
    if zero:
        zero -= 1
    else:
        ans += m

while len(plus) > 1:
    ans += plus.pop() * plus.pop()

print(ans + sum(plus) + one)
