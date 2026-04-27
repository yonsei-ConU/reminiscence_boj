import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, lK = minput()
K = input_().split()
if lK == 1:
    print(K[0])
elif lK == 2:
    ans = 0
    for perm in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        a, b = perm
        if int(K[a] + K[b]) <= N:
            ans = max(ans, int(K[a] + K[b]))
    if not ans:
        if int(K[0]) <= N:
            ans = int(K[0])
        if int(K[1]) <= N:
            ans = max(ans, int(K[1]))
    print(ans)
else:
    assert lK == 3
    ans = 0
    for perm in [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]:
        a, b, c = perm
        if int(K[a] + K[b] + K[c]) <= N:
            ans = max(ans, int(K[a] + K[b] + K[c]))
    if not ans:
        for perm in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
            a, b = perm
            if int(K[a] + K[b]) <= N:
                ans = max(ans, int(K[a] + K[b]))
    if not ans:
        if int(K[0]) <= N:
            ans = int(K[0])
        if int(K[1]) <= N:
            ans = max(ans, int(K[1]))
        if int(K[2]) <= N:
            ans = max(ans, int(K[2]))
    print(ans)
