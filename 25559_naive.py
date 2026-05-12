import sys
from itertools import permutations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for i in range(1, 11):
    print("*" * 30 + str(i) + "*" * 30)
    for p in permutations(range(1, i + 1)):
        chk = [False] * i
        cur = 0
        for v in p:
            cur += v
            if cur >= i:
                cur -= i
            chk[cur] = True
        if False not in chk:
            print(*p)
