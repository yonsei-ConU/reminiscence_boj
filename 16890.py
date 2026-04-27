import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


K = input_().rstrip()
C = input_().rstrip()
k = [0] * 26
c = [0] * 26
for a in K:
    k[ord(a) - 97] += 1
for a in C:
    c[ord(a) - 97] += 1

k = k[::-1]
    
ans = []
for i in range(len(K)):
    while not k[-1]:
        k.pop()
    while not c[-1]:
        c.pop()
    if i & 1:
        c[-1] -= 1
        ans.append(chr(len(c) + 96))
    else:
        k[-1] -= 1
        ans.append(chr(97 + 26 - len(k)))

print(''.join(ans))
