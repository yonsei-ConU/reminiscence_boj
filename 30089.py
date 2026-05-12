import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    S = input_().rstrip()
    a = 21
    for k in range(len(S))[::-1]:
        if S[k:] == S[k:][::-1]:
            a = min(a, k)
    print(S + S[:a][::-1])
