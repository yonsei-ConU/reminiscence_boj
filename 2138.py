import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
cur = input_().rstrip()
goal = input_().rstrip()
A = []
for i in range(N):
    if cur[i] == goal[i]:
        A.append(0)
    else:
        A.append(1)
B = A[:]
t = 0
for i in range(1, N):
    if A[i - 1]:
        t += 1
        A[i - 1] ^= 1
        A[i] ^= 1
        if i != N - 1:
            A[i + 1] ^= 1

if 1 not in A:
    ans = t
else:
    ans = 10 ** 8

t = 1
A = B
A[0] ^= 1
A[1] ^= 1
for i in range(1, N):
    if A[i - 1]:
        t += 1
        A[i - 1] ^= 1
        A[i] ^= 1
        if i != N - 1:
            A[i + 1] ^= 1

if 1 not in A:
    ans = min(ans, t)

if ans == 10 ** 8:
    print(-1)
else:
    print(ans)
