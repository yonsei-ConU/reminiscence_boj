import sys
from math import gcd
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, K = minput()
numbers = [0] * N
for i in range(M - 1):
    a, b, c = map(lambda x: int(x) - 1, input_().split())
    numbers[a] += 1
    numbers[b] += 1
    numbers[c] += 1

s = sum(numbers) + 3
ans_prob = -1
ans_construct = [-1, -1, -1]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or i == k or j == k:
                continue
            lst = {i, j, k}
            prob = [numbers[x] + (x in lst) for x in range(N)]
            appear_prob = prob[i] + prob[j] + prob[k]
            cur_prob = (s - appear_prob) ** K * appear_prob
            if cur_prob > ans_prob:
                ans_prob = cur_prob
                ans_construct = [i + 1, j + 1, k + 1]

num, den = ans_prob, s ** (K + 1)
g = gcd(num, den)
num //= g
den //= g
print(num, den)
print(*ans_construct)
