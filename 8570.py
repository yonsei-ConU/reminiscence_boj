import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
s = input_().strip()

cnt = 0
depth = []
stack = []

for paren in s:
    if paren == '(':
        cnt += 1
        stack.append('(')
    else:
        cnt -= 1
        if stack:
            depth.append(cnt)
            stack.pop()

ans = 0
stack = []
stack_ps = []
last = 0
for c in depth:
    if last - c > 1:
        pass
    elif last - c == 1:
        stack = [stack_ps[-1] + 1]
        stack_ps = [stack[0]]
    elif last == c:
        pass
    else:
        stack.append(1)
        if not stack_ps:
            stack_ps = [1]
        else:
            stack_ps.append(stack_ps[-1] + 1)
