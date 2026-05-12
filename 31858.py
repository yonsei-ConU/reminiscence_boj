# 17m 11.41s

import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if N == 1: exit(print(0))
P = list(minput())
stack = [P[0]]
ans = 0

for i in range(1, N):
    t = P[i]
    while stack and t > stack[-1]:
        stack.pop()
        ans += 1
    if stack: ans += 1
    stack.append(t)

print(ans)
