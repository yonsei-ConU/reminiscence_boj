import sys
input_ = sys.stdin.readline
def mfnput(): return map(float, input_().split())


N = int(input_())
R = list(mfnput())
S = input_().rstrip()
stack = [[[], 0]]

for c in S:
    if c == '(':
        stack.append([[], 0])
    elif c == 'R':
        continue
    elif c.isdigit():
        c = int(c) - 1
        stack[-1][0].append(R[c])
    elif c == '-':
        stack[-1][1] = 1
    elif c == '|':
        stack[-1][1] = 2
    elif c == ')':
        lst, v = stack.pop()
        if v == 2:
            x = 1 / sum(1 / t for t in lst)
        else:
            x = sum(lst)
        stack[-1][0].append(x)

assert len(stack) == 1 and len(stack[0][0]) == 1
print(stack[0][0][0])
