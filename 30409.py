import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())
def dist2(A, B): return (H[A] - H[B]) ** 2 + (A - B) ** 2


N = int(input_())
H = list(minput())
larger_right = [None] * N
stack = []
for i in range(N)[::-1]:
    while stack and H[stack[-1]] < H[i]:
        stack.pop()
    if stack:
        larger_right[i] = stack[-1]
    stack.append(i)

larger_left = [None] * N
stack = []
for i in range(N):
    while stack and H[stack[-1]] < H[i]:
        stack.pop()
    if stack:
        larger_left[i] = stack[-1]
    stack.append(i)

lr_cost = [0] * N
for i in range(N):
    t = larger_left[i]
    if t is None:
        continue
    lr_cost[i] = max(lr_cost[i], lr_cost[t] + dist2(i, t))

rl_cost = [0] * N
for i in range(N)[::-1]:
    t = larger_right[i]
    if t is None:
        continue
    rl_cost[i] = max(rl_cost[i], rl_cost[t] + dist2(i, t))
'''print('', lr_cost, rl_cost, sep="""
""")'''
for _ in range(int(input_())):
    query = int(input_()) - 1
    print(lr_cost[query] + rl_cost[query])
