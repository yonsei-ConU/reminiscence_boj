import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
S = list(minput())
ans = 1
ptr = 0
while ptr < N - 1:
    if S[ptr] > S[ptr + 1]:
        d = 1
        while ptr + d < N and ptr - d >= 0 and S[ptr + d] == S[ptr - d] and S[ptr + d - 1] > S[ptr + d]:
            d += 1
        d -= 1
        if d:
            ans = max(ans, 2 * d + 1)
            ptr += d
        else:
            ptr += 1
    elif S[ptr] == S[ptr + 1]:
        d = 1
        while ptr + d < N and ptr + 1 - d >= 0 and S[ptr + d] == S[ptr + 1 - d] and (d == 1 or S[ptr + d - 1] > S[ptr + d]):
            d += 1
        d -= 1
        if d:
            ans = max(ans, 2 * d)
            ptr += d
        else:
            ptr += 1
    else:
        ptr += 1

print(ans)
