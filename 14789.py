import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    s, K = input_().split()
    K = int(K)
    S = [1 if i == '+' else 0 for i in s]
    L = len(S)
    ans = 0
    i = 0
    
    while i <= L - K:
        if S[i] == 0:
            ans += 1
            for j in range(K):
                S[i + j] ^= 1
        i += 1

    if 0 not in S:
        print(f"Case #{tc}: {ans}")
    else:
        print(f"Case #{tc}: IMPOSSIBLE")
