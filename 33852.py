import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


s = input_().rstrip()
S = []
for c in s:
    S.append(int(c, 36))
S = S[::-1]

k, p = minput()

if len(S) == 1 and k >= 36:
    exit(print(-1))

pow36 = [1]
for i in range(len(s)):
    pow36.append(pow36[-1] * 36 % p)

t = sum(S[i] * pow36[i] for i in range(len(S))) % p
if not (t - k) % p:
    exit(print(0))

for i in range(len(S)):
    for m in range(t - S[i] * pow36[i], t - S[i] * pow36[i] + 36 * pow36[i], pow36[i]):
        if not (m - k) % p:
            exit(print(1))

print(2)
