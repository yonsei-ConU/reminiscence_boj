import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


S = input_().rstrip()
P = input_().rstrip()
ptr = 0
ans = 0

while ptr < len(P):
    ans += 1

    nextptr = ptr + 1
    while nextptr <= len(P) and P[ptr:nextptr] in S:
        nextptr += 1

    ptr = nextptr - 1

print(ans)
