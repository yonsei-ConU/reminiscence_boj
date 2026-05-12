import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


S = input_().rstrip()
if S != S[::-1]:
    print(len(S))
elif len(set(S)) == 1:
    print(-1)
else:
    print(len(S) - 1)
