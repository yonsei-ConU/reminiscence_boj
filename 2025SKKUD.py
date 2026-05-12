import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
outdeg = [0] * N
for _ in range(M):
    a, b = minput()
    outdeg[a - 1] += 1

print(outdeg.count(1))
