import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
stack = []
H = [0] + list(A) + [0]
ps = [0]
for i in range(1, N + 2):
    ps.append(ps[-1] + H[i])

ans = 0
ans_range = (1, 1)
for i in range(N + 2):
    start_idx = i
    while stack and stack[-1][0] > H[i]:
        height, start_idx = stack.pop()
        if height * (ps[i - 1] - ps[start_idx - 1]) > ans:
            ans = height * (ps[i - 1] - ps[start_idx - 1])
            ans_range = (start_idx, i - 1)
    if not stack or stack[-1][0] < H[i]:
        stack.append((H[i], start_idx))

print(ans)
print(*ans_range)
