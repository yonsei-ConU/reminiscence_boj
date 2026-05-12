import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def z(s):
    ret = [0] * len(s)
    l = r = 0
    ret[0] = len(s)
    for i in range(1, len(s)):
        if i > r:
            l = r = i
            while r < len(s) and s[r - l] == s[r]: r += 1
            r -= 1
            ret[i] = r - l + 1
        else:
            if ret[i - l] < r - i + 1: ret[i] = ret[i - l]
            else:
                l = i
                while r < len(s) and s[r - l] == s[r]: r += 1
                r -= 1
                ret[i] = r - l + 1
    return ret


S = input_().rstrip()[::-1]
Z = z(S)
for _ in range(int(input_())):
    print(Z[len(S) - int(input_())])
