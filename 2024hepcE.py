import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_())
A = list(minput())
a = A[:]

cnt = 0
for i in range(len(a) - 1, -1, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            cnt += 1
ans = cnt
cnt = 1
a = A[:]
for i in range(len(a) - 1, -1, -1):
    for j in range(i):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            cnt += 1
print(min(ans, cnt))
