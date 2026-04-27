import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def fail(s2):
    ret = [0] * len(s2)
    j = 0
    for i in range(1, len(s2)):
        while j > 0 and s2[i] != s2[j]:
            j = ret[j - 1]

        if s2[i] == s2[j]:
            j += 1
            ret[i] = j
    return ret


while True:
    s = input_().rstrip() * 2
    N = len(s)
    if s == '..':
        break
    f = N - max(fail(s))
    print(N // 2 // f)
