import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def f():
    global ans
    if len(stack) < 5:
        return False
    if stack[-5] != 's':
        return False
    for i in range(4):
        if stack[i - 4] != keep[i] and stack[i - 4] != '*':
            return False
    for i in range(5):
        stack.pop()
    stack.append('*')
    ans += 1
    return True


keep = "keep"
N = int(input_())
S = input_().rstrip()
ans = 0
stack = []
for c in S:
    stack.append(c)
    while True:
        if not f():
            break

print(ans)
