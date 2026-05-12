import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    S, n = input_().split()
    n = int(n)
    L = len(S)
    consonant = [False] * L
    for i in range(L):
        if S[i] not in 'aeuio':
            consonant[i] = True
    ans = 0
    last = 0
    streak = 0
    for i in range(L):
        if consonant[i]:
            streak += 1
            if streak >= n and i - n - last + 2 > 0:
                ans += (i - n - last + 2) * (L - i)
                last = i - n + 2
        else:
            streak = 0
    print(f"Case #{tc}: {ans}")
