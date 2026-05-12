import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, A, B = minput()
T = sorted(list(minput()))
time = 0
completed = 0
ans = 0
for sleep_point in range(N):
    for x in range(1, A):
        t = time + B * x
        a = A - x
        c = completed
        for i in range(sleep_point, N):
            if t + a <= T[i]:
                c += 1
                t += a
        ans = max(ans, c)
    if time + A <= T[sleep_point]:
        completed += 1
        time += A
        ans = max(ans, completed)

print(ans)
