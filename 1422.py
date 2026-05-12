import sys
from functools import cmp_to_key
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def cmp(s1, s2):
    first = s1 + s2
    second = s2 + s1
    if first > second:
        return -1
    elif first == second:
        return 0
    else:
        return 1


def cmp2(s1, s2):
    if len(s1) > len(s2):
        return -1
    elif len(s1) < len(s2):
        return 1
    else:
        return cmp(s1, s2)


K, N = minput()
lst = [input_().rstrip() for _ in range(K)]
if set(lst) == {'0'}: exit(print(0))
lst.sort(key=cmp_to_key(cmp))
inject_first = sorted(lst, key=cmp_to_key(cmp2))[0]
idx = lst.index(inject_first)
print(''.join(lst[:idx]) + lst[idx] * (N - K) + ''.join(lst[idx:]))
