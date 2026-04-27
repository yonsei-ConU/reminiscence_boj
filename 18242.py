import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
up = -1
left = 0
right = -1
for i in range(N):
    t = input_().rstrip()
    if up == -1 and '#' in t:
        up = i
        if '#.#' in t:
            print('UP')
            exit()
        sharp = False
        for j in range(M):
            if t[j] == '#' and not sharp:
                left = j
                sharp = True
            elif t[j] == '.' and sharp:
                right = j - 1
                break
        else:
            right = M - 1
    elif i - up >= right - left and up > -1:
        print('DOWN')
        exit()
    elif up > -1:
        if t[left] == '.':
            print('LEFT')
            exit()
        elif t[right] == '.':
            print('RIGHT')
            exit()
print('DOWN')
