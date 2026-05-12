import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans = 0
stack = []
d = 0

for i in range(N):
    height = int(input_())
    while stack and stack[-1][0] < height:
        p, q = stack.pop()
        d -= q
        ans += q
    # ans += bool(stack)
    if stack and stack[-1][0] == height:
        p, q = stack.pop()
        ans += bool(stack)
        ans += q
        stack.append((p, q + 1))
    else:
        ans += bool(stack)
        stack.append((height, 1))
    d += 1

print(ans)
