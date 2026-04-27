import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


ans = [-2] * (2 ** 15)
ans[0] = -1


def flip(x, l, r):
    k = x.bit_length()
    l, r = k - r - 1, k - l - 1
    return x ^ (((1 << (r - l + 1)) - 1) << l)


def dp(n):
    if ans[n] != -2:
        return ans[n]
    l = n.bit_length()
    check = 0
    for i in range(l):
        for j in range(i, l):
            if n & (1 << (l - j - 1)) and dp(flip(n, i, j)) == -1:
                ans[n] = 1
                return ans[n]
    ans[n] = -1
    return ans[n]


for _ in range(int(input_())):
    S = input_().strip()[::-1]
    state = 0
    for i in range(len(S)):
        if S[i] == 'H':
            state += 1 << i
    res = dp(state)
    if res == -1:
        print('NO')
    else:
        ans_i = -1
        ans_j = 16
        for a in range(state.bit_length()):
            for b in range(a, state.bit_length()):
                # print(bin(state), a, b, bin(flip(state, a, b)))
                if state.bit_length() & (1 << (state.bit_length() - b - 1)) and dp(flip(state, a, b)) == -1:
                    i = b + 1
                    j = b - a + 1
                    if i > ans_i:
                        ans_i = i
                        ans_j = j
                    elif i == ans_i:
                        ans_j = min(j, ans_j)
        print('YES', ans_i, ans_j)
