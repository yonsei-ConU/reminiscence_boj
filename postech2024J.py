import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, k = minput()
S = list(input_().rstrip())
start = 0

while 1:
    x = ord(S[start])
    if 91 - x <= k and x != 65:
        S[start] = 'A'
        k -= 91 - x
        if not k:
            break
    start += 1
    if start == N:
        break

S[-1] = chr(ord(S[-1]) + k % 26)
print(''.join(S))
