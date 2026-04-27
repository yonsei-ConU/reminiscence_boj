import sys
from itertools import permutations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def pcd(l, permutation):
    processed = [False] * l
    cycles = 0
    for i in range(l):
        if processed[i]:
            continue     
        cycle = []
        pointer = i
        while not processed[pointer]:
            processed[pointer] = True     
            cycle.append(pointer)
            pointer = permutation[pointer]
        if cycle:
            cycles += 1

    return cycles


N = int(input_())
domino = []
for _ in range(N):
    t = list(input_().strip())
    row = []
    for num in t:
        if num.isdigit():
            row.append(int(num))
        else:
            row.append(64 - ord(num))
    domino.append(row)

res = []
for p in permutations(range(N), N):
    score = 1
    cur_domino = []
    for i in range(N):
        score *= domino[i][p[i]]
    if not pcd(N, p) % 2:
        score *= -1
    res.append(score)

print(min(res))
print(max(res))
