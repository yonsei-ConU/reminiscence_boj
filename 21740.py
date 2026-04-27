import sys
from functools import cmp_to_key
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def cmp(s1, s2):
    table = str.maketrans("69", "96")
    first = (s1 + s2).translate(table)[::-1]
    second = (s2 + s1).translate(table)[::-1]
    breakpoint()
    if first > second:
        return -1
    elif first == second:
        return 0
    else:
        return 1
    s3 = s1 + s2
    s4 = s2 + s1
    for i in range(len(s3) - 1, -1, -1):
        if s3[i] == '6' and s4[i] == '9':
            return -1
        elif s3[i] == '9' and s4[i] == '6':
            return 1
        elif s3[i] > s4[i]:
            return -1
        elif s3[i] < s4[i]:
            return 1
    return 0


def cmp2(s1, s2):
    if len(s1) > len(s2):
        return -1
    elif len(s1) < len(s2):
        return 1
    else:
        return cmp(s1, s2)


N = int(input_())
lst = input_().rstrip().split()
print(lst)
lst.sort(key=cmp_to_key(cmp))
inject_first = sorted(lst, key=cmp_to_key(cmp2))[-1]
idx = lst.index(inject_first)
print(''.join(lst[:idx]) + lst[idx] + ''.join(lst[idx:]))
