import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def make_roman(n):
    if n == 1000:
        return 'M'
    res = ''
    if n >= 900:
        n -= 900
        res += 'CM'
    elif n >= 500:
        n -= 500
        res += 'D'
    elif n >= 400:
        n -= 400
        res += 'CD'
    res += 'C' * (n // 100)
    n %= 100
    if n >= 90:
        n -= 90
        res += 'XC'
    elif n >= 50:
        n -= 50
        res += 'L'
    elif n >= 40:
        n -= 40
        res += 'XL'
    res += 'X' * (n // 10)
    n %= 10
    res += ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'][n]
    return res


pre = list(range(1, 1001))
pre.sort(key=make_roman)
front = 945
back = 54
late = pre[946:]

for _ in range(int(input_())):
    p = int(input_())
    x, y = divmod(p, 1000)
    if y in late:
        # 뒤에서부터 세야 하는 수
        idx = late.index(y)
        print(-(x * back + 54 - idx))
    elif y:
        # 앞에서부터 세야 하는 수
        idx = pre.index(y)
        print(946 * x + idx + 1)
    else:
        print(946 * x)
