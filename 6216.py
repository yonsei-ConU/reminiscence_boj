import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
tasks = []
for i in range(N):
    T, S = minput()
    tasks.append((-S / T, i + 1))

tasks.sort()
for _, i in tasks: print(i, end=' ')
