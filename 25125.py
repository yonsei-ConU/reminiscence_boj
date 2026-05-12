import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    N, K = minput()
    E = list(minput())
    prod = 0
    for i in range(N):
        for j in range(i):
            prod += E[i] * E[j]
    s = sum(E)
    if N == 1 or not prod:
        print(f"Case #{tc}: 0")
        continue
    elif K == 1:
        if not s or prod % s:
            print(f"Case #{tc}: IMPOSSIBLE")
        else:
            print(f"Case #{tc}: {-prod // s}")
    else:
        print(f"Case #{tc}:", 1 - s, s * s - s - prod)
