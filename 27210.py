import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
direction = list(minput())
kadane = []
for i in range(N):
    if direction[i] == 1:
        kadane.append(1)
    else:
        kadane.append(-1)

for i in range(1, N):
    kadane[i] = max(kadane[i - 1] + kadane[i], kadane[i])

ans = max(kadane)
kadane = []
for i in range(N):
    if direction[i] == 2:
        kadane.append(1)
    else:
        kadane.append(-1)

for i in range(1, N):
    kadane[i] = max(kadane[i - 1] + kadane[i], kadane[i])

print(max(max(kadane), ans))
