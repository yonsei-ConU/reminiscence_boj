import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
start = {input_().rstrip(): i for i in range(N)}
start_rev = {start[k]: k for k in start}

pointer = 0
ans = 0
came = set()
for i in range(N):
    end = input_().rstrip()
    came.add(end)
    k = start[end]
    if k == pointer:
        while pointer < N and start_rev[pointer] in came:
            pointer += 1
    else:
        ans += 1

print(ans)
