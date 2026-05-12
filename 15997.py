import sys
from fractions import Fraction
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


c = input_().split()
countries = {c[i]: i for i in range(4)}
results = []

for _ in range(6):
    A, B, W, D, L = input_().split()
    A = countries[A]
    B = countries[B]
    W = Fraction(W)
    D = Fraction(D)
    L = Fraction(L)
    results.append((A, B, W, D, L))

ans = [Fraction('0') for _ in range(4)]

for i in range(3 ** 6):
    j = i
    total_prob = Fraction('1')
    scores = [0, 0, 0, 0]
    for idx in range(6):
        wdl = j % 3
        A, B, *prob = results[idx]
        if not wdl:
            # 승리
            scores[A] += 3
        elif wdl == 1:
            scores[A] += 1
            scores[B] += 1
        else:
            scores[B] += 3
        total_prob *= prob[wdl]
        j //= 3
    distinct = sorted(set(scores), reverse=True)
    m = distinct[0]
    win = []
    for x in range(4):
        if scores[x] == m:
            win.append(x)
    if len(win) >= 2:
        for w in win:
            ans[w] += total_prob * 2 / len(win)
    else:
        ans[win[0]] += total_prob
        m = distinct[1]
        second_win = []
        for x in range(4):
            if scores[x] == m:
                second_win.append(x)
        for w in second_win:
            ans[w] += total_prob / len(second_win)

for a in ans:
    print(a.numerator / a.denominator)
