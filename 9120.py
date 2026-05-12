import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def knuth_morris_pratt(s2, s1):
    fail = [0] * len(s2)
    j = 0

    for i in range(1, len(s2)):

        while j > 0 and s2[i] != s2[j]:
            j = fail[j-1]

        if s2[i] == s2[j]:
            j += 1
            fail[i] = j

    result = []
    j = 0

    for i in range(len(s1)):

        while j > 0 and s1[i] != s2[j]:
            j = fail[j-1]

        if s1[i] == s2[j]:
            if j + 1 == len(s2):
                result.append(i + 2 - len(s2))
                j = fail[j]
            else:
                j += 1

    return result


for _ in range(int(input_())):
    print(len(knuth_morris_pratt(input_().rstrip(), input_().rstrip())))
