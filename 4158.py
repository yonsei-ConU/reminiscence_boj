import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    N, M = minput()
    if N == M == 0:
        break
    s = set()
    for _ in range(N):
        s.add(int(input_()))

    ans = 0
    for _ in range(M):
        if int(input_()) in s:
            ans += 1

    print(ans)
