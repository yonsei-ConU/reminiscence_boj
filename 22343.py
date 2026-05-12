import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def eval_paren(pp):
    stack = []
    depth = 0
    for p in pp:
        if p == '(':
            depth += 1
        else:
            depth -= 1
            if not stack or stack[-1][1] < depth:
                stack.append((1, depth))
            elif stack[-1][1] == depth:
                val, _ = stack.pop()
                stack.append((val + 1, depth))
            else:
                val, _ = stack.pop()
                val *= 2
                if stack and stack[-1][1] == depth:
                    val2, _ = stack.pop()
                    val += val2
                stack.append((val, depth))

    ret = 0
    for value, depth in stack:
        ret += value
    return ret


from time import time
for _ in range(int(input_())):
    A = input_().rstrip()
    B = input_().rstrip()
    start = time()
    a = eval_paren(A)
    b = eval_paren(B)
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')
    print(time() - start)
