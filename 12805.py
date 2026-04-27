import sys
from itertools import combinations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    s = input_().rstrip()
    n = len(s)
    k = int(input_())
    if n >= 15:
        print('YES')
        i = 0
        for i in range(1, k):
            print(s[i * (i - 1) // 2:i * (i + 1) // 2])
        print(s[i * (i + 1) // 2:])
        continue
    lst = list(range(1, n))
    for p in list(combinations(lst, k - 1)):
        t = []
        p_ = [0] + list(p) + [n]
        for i in range(len(p_) - 1):
            t.append(s[p_[i]:p_[i+1]])
        if len(set(t)) == k:
            print('YES')
            print('\n'.join(t))
            break
    else:
        print('NO')
