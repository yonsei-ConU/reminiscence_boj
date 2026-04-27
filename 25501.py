import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    S = input_().rstrip()
    ans = 0
    l = 0
    r = len(S) - 1
    while l < r:
        ans += 1
        if S[l] != S[r]:
            break
        l += 1
        r -= 1
    ans2 = +(S == S[::-1])
    print(ans2, ans + ans2)
