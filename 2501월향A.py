import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, K = minput()
unavailable = set()
ans = []
ptr = 1
while len(ans) < N:
    if ptr > M:
        exit(print(-1))
    ans.append(ptr)
    unavailable.add(ptr ^ K)
    ptr += 1
    while ptr in unavailable:
        ptr += 1

print(*ans)
