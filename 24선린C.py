import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
log = []
d = {'teacher': 0, 'student': 1}
for _ in range(N + 1):
    time, person = input_().split()
    time = time.split(':')
    time = int(time[0]) * 60 + int(time[1])
    log.append((time, d[person]))

T = input_().rstrip().split(':')
T = int(T[0]) * 60 + int(T[1])
log.sort()
ans = 0
check = 0

for i in range(N + 1):
    flag = 0
    if not check & 1 and log[i][0] >= T:
        check |= 1
        flag = 1
    if not check & 2 and not log[i][1]:
        check |= 2
        flag = 1
    if check == 3 and log[i][1]:
        ans += 1

print(ans)
