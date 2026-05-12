import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, m, r = minput()
r -= 1
frozen = [[i] + list(input_().rstrip()) for i in range(n)]
ptr = n - 1
while ptr >= 0:
    if 'P' in frozen[ptr]:
        d = input_().count('y') - 3
        p = frozen[ptr].index('P')
        frozen[ptr][p] = 'asdfasdf'
        if d > 0:
            frozen = frozen[:ptr - d] + [frozen[ptr]] + frozen[ptr - d:ptr] + frozen[ptr + 1:]
    else:
        ptr -= 1

for i in range(len(frozen)):
    if frozen[i][0] == r:
        exit(print(i + 1))

assert False
