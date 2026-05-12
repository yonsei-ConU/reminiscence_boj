import sys
# sys.stdin = open('data.txt')
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def LCS(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0 for i in range(len2+1)] for j in range(len1+1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    res = []
    i = len1
    j = len2
    while i > 0 and j > 0:
        t = dp[i][j]
        if dp[i - 1][j] == t:
            i -= 1
        elif dp[i][j - 1] == t:
            j -= 1
        else:
            res.append(str1[i-1])
            i -= 1; j -= 1
    return ''.join(res)[::-1]


for fruit in sys.stdin:
    fruit = fruit.split()
    lcs = LCS(fruit[0], fruit[1])
    lastptr0 = lastptr1 = 0
    res = ''

    for ptrLCS in range(len(lcs)):
        ptr0 = lastptr0
        ptr1 = lastptr1
        while fruit[0][ptr0] != lcs[ptrLCS]:
            ptr0 += 1
        while fruit[1][ptr1] != lcs[ptrLCS]:
            ptr1 += 1
        res += fruit[0][lastptr0:ptr0] + fruit[1][lastptr1:ptr1] + lcs[ptrLCS]
        lastptr0, lastptr1 = ptr0 + 1, ptr1 + 1

    res += fruit[0][lastptr0:] + fruit[1][lastptr1:]
    print(res)
