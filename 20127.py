import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
a = list(minput())
if N <= 2 or len(set(a)) == 1:
    exit(print(0))
cnt = 0
t = -1
fuck = 0
for i in range(1, N):
    if a[i] < a[i - 1]:
        cnt += 1
        t = i
    if cnt > 1:
        fuck = 0
        break
else:
    if a[-1] <= a[0] or not cnt:
        fuck = t

trashproblem = 0
t = -1
cnt = 0
for i in range(1, N):
    if a[i] > a[i - 1]:
        cnt += 1
        t = i
    if cnt > 1:
        trashproblem = 0
        break
else:
    if a[-1] >= a[0] or not cnt:
        trashproblem = t

if fuck == trashproblem == -1:
    print(0)
elif fuck and trashproblem:
    print(min(fuck, trashproblem))
elif fuck:
    print(fuck)
elif trashproblem:
    print(trashproblem)
else:
    print(-1)
