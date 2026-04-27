import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def manacher(s):
    """
    :param: s: the string
    change dummy_char if necessary
    """
    dummy_char = '#'
    S = [''] * (2 * len(s) - 1)
    for i in range(len(s)):
        S[2 * i] = s[i]
    for i in range(len(s) - 1):
        S[2 * i + 1] = dummy_char
    dp = [0] * len(S)
    j = r = -1
    for i in range(N):
        if i > r:
            # 겹치지 않으므로 나이브
            l = 
            
