import sys
from functools import cmp_to_key
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def cmp(a, b):
    if a == b:
        return 0
    for x, y in zip(a, b):
        if x == y:
            continue
        elif x.isdigit() and not y.isdigit():
            return -1
        elif not x.isdigit() and y.isdigit():
            return 1
        elif x.isdigit() and y.isdigit():
            if int(x) > int(y):
                return 1
            elif int(x) < int(y):
                return -1
            elif x.count('0') > y.count('0'):
                return 1
            else:
                return -1
        else:
            table = str.maketrans('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
            if x.translate(table) > y.translate(table):
                return 1
            else:
                return -1
    if len(a) > len(b):
        return 1
    else:
        return -1
    assert False


N = int(input_())
A = []

for _ in range(N):
    s = input_().rstrip()
    tmp = []
    digit = ''
    string = ''
    for char in s:
        if char.isdigit():
            digit += char
            if string:
                tmp.append(string)
            string = ''
        else:
            string += char
            if digit:
                tmp.append(digit)
            digit = ''
    if digit:
        tmp.append(digit)
    if string:
        tmp.append(string)
    A.append(tmp)

A.sort(key=cmp_to_key(cmp))
for a in A:
    print(''.join(a))
