import sys
from collections import Counter
from math import factorial
from itertools import permutations as perm
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
S = tuple(input_().rstrip())
c = Counter(S)

comb = [[0 for i in range(N + 1)] for j in range(N + 1)]
for n in range(N + 1):
    for k in range(n + 1):
        if k == 0 or k == n:
            comb[n][k] = 1
        else:
            comb[n][k] = comb[n - 1][k - 1] + comb[n - 1][k]

front = 0
spaces_left = N
mult = 1
keys = sorted(c.keys(), reverse=True)
for key in keys:
    tmp = 0
    diff = spaces_left
    while spaces_left - diff < c[key]:
        tmp += comb[spaces_left][spaces_left - diff] * int(key) ** (diff)
        diff -= 1
    tmp *= mult
    front += tmp
    mult *= comb[spaces_left][c[key]]
    spaces_left -= c[key]

# 순열 생성 및 정렬 대신 직접 순서 계산
chars = sorted(set(S), reverse=True)
char_count = Counter(S)
order = 0

for i, char in enumerate(S):
    for c in chars:
        if c > char:
            if char_count[c] > 0:
                temp_count = char_count.copy()
                temp_count[c] -= 1
                perm_count = 1
                for j in range(N - i - 1, 0, -1):
                    perm_count *= j
                for count in temp_count.values():
                    for j in range(count, 0, -1):
                        perm_count //= j
                order += perm_count
        elif c == char:
            char_count[c] -= 1
            break

print(front + order)
