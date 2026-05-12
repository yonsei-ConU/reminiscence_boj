import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
alphabet = [0] * 10
nonzero = [False] * 10
for _ in range(N):
    s = input_().rstrip()[::-1]
    nonzero[ord(s[-1]) - 65] = True
    for i in range(len(s)):
        alphabet[ord(s[i]) - 65] += 10 ** i

alphabet = [[alphabet[i], nonzero[i]] for i in range(10)]
alphabet.sort()
ans = 0
chk = False
new_alphabet = []
for a, n in alphabet:
    if not chk and not n:
        chk = True
    else:
        new_alphabet.append(a)
print(sum(new_alphabet[i] * (i + 1) for i in range(9)))
