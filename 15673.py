import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
P = list(minput())

KADANE = P[:]
TRACE = [0] * N
for i in range(1, N):
    if KADANE[i - 1] > 0:
        TRACE[i] = TRACE[i - 1]
    else:
        TRACE[i] = i
    KADANE[i] = max(KADANE[i - 1] + KADANE[i], KADANE[i])

PM = [KADANE[0]]
for i in range(1, N):
    PM.append(max(PM[-1], KADANE[i]))

kadane = P[:]
trace = [0] * N
for i in range(1, N):
    if kadane[i - 1] < 0:
        trace[i] = trace[i - 1]
    else:
        trace[i] = i
    kadane[i] = min(kadane[i - 1] + kadane[i], kadane[i])

pm = [kadane[0]]
for i in range(1, N):
    pm.append(min(pm[-1], kadane[i]))
print(TRACE)
print(trace)
ans = 0
for i in range(1, N):
    idx = TRACE[i] - 1
    if idx != -1:
        ans = max(ans, (KADANE[i] - KADANE[idx]) * KADANE[idx])
    idx = trace[i] - 1
    if idx != -1:
        ans = max(ans, (kadane[i] - kadane[idx]) * kadane[idx])

print(ans)
