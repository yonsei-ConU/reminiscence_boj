from itertools import permutations as pp

N = 4
for p in list(pp(range(N), N)):
    check = True
    for i in range(1, N - 1):
        if max(min(p[:i]), min(p[i + 1:])) < p[i]:
            check = False
            break
    if check:
        print(*p)
