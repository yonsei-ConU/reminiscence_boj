import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MOD = 998244353
factmod = [1, 1]
for i in range(2, 100001):
    factmod.append(factmod[-1] * i % MOD)

N = int(input_())
students = []
cminusa = defaultdict(int)
for i in range(N):
    c, a = minput()
    students.append((c - a, c, a, i + 1))
    cminusa[c - a] += 1

kind = 1
for v in cminusa.values():
    kind = (kind * factmod[v]) % MOD

students.sort(reverse=True)
min_score = sum(students[i][1] * i + students[i][2] * (N - 1 - i) for i in range(N))
max_score = sum(students[i][1] * (N - 1 - i) + students[i][2] * i for i in range(N))
trace = [students[i][3] for i in range(N)]
print(min_score, kind)
print(*trace)
print(max_score, kind)
print(*trace[::-1])
