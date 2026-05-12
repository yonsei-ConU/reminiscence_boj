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


N = int(input_())
lst = input_().split()
if set(lst) == {'0'}: exit(print(0))
lst.sort(key=cmp_to_key(cmp))
print(''.join(lst))
