import sys
from math import gcd
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def egcd(a, b):
    if not b:
        return 1, 0
    else:
        x, y = egcd(b, a % b)
        return y, x - (a // b) * y


N, A, B, Da, Db = minput()
# A + k1 * Da = B - k2 * Db (mod N)
# k1 * Da + k2 * Db = B - A (mod N)
g = gcd(Da, Db, N)
newDa = Da // g
newDb = Db // g
if gcd(newDa, newDb) != 1:
    exit(print('Evil Galazy'))
newN = N // g
# equation: k1 * newDa + k2 * newDb = (B - A) / g (modnewN)
if (B - A) % g:
    exit(print('Evil Galazy'))
# solve k1 * newDa + k2 * newDb = 1 (modnewN) first
k1, k2 = egcd(newDa, newDb)
# k1, k2 is the solution, so go to k1 * newDa + k2 * newDb = (B - A) / g (modnewN)
C = ((B - A) // g) % newN
k1 = (k1 * C) % newN
k2 = (k2 * C) % newN

ans = 99999999
for i in range(newN):
    print(k1, k2)
    if 1 in [(k1 - k2) % newN, (k2 - k1) % newN] or newN - 1 in [(k1 - k2) % newN, (k2 - k1) % newN]:
        ans = min(ans, k1 + k2)
    elif 1 in [(k1 - k2 + newDa) % newN, (k1 - k2 - newDa) % newN] or newN - 1 in [(k1 - k2 + newDa) % newN, (k1 - k2 - newDa) % newN]:
        ans = min(ans, k1 + k2 + 1)
    k1 = (k1 + newDb) % newN
    k2 = (k2 - newDa) % newN

print(ans)
