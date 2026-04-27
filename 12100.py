import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def go_up(b):
    for j in range(N):
        wnf = [b[i][j] for i in range(N) if b[i][j]]
        stack = []
        for element in wnf:
            if stack and stack[-1] == element:
                stack.pop()
                stack.append(element * 2)
                stack.append(-1)
            elif element:
                stack.append(element)
        res = [x for x in stack if x != -1] + [0] * 20
        for i in range(N):
            b[i][j] = res[i]
    return b


def go_down(b):
    for j in range(N):
        wnf = [b[i][j] for i in range(N-1, -1, -1) if b[i][j]]
        stack = []
        for element in wnf:
            if stack and stack[-1] == element:
                stack.pop()
                stack.append(element * 2)
                stack.append(-1)
            elif element:
                stack.append(element)
        res = [x for x in stack if x != -1] + [0] * 20
        for i in range(N):
            b[i][j] = res[N - 1 - i]
    return b


def go_left(b):
    for i in range(N):
        wnf = b[i][:]
        stack = []
        for element in wnf:
            if stack and stack[-1] == element:
                stack.pop()
                stack.append(element * 2)
                stack.append(-1)
            elif element:
                stack.append(element)
        res = [x for x in stack if x != -1] + [0] * 20
        for j in range(N):
            b[i][j] = res[j]
    return b


def go_right(b):
    for i in range(N):
        wnf = b[i][::-1]
        stack = []
        for element in wnf:
            if stack and stack[-1] == element:
                stack.pop()
                stack.append(element * 2)
                stack.append(-1)
            elif element:
                stack.append(element)
        res = [x for x in stack if x != -1] + [0] * 20
        for j in range(N):
            b[i][j] = res[N - 1 - j]
    return b


N = int(input_())
board = [list(minput()) for _ in range(N)]
ans = 0
func_list = [go_up, go_down, go_left, go_right]
for i in range(1024):
    b = [x[:] for x in board]
    for j in range(0, 10, 2):
        direction = (i & ((1 << j) | (1 << (j + 1)))) >> j
        func_list[direction](b)
    ans = max(ans, max(max(row) for row in b))

print(ans)
