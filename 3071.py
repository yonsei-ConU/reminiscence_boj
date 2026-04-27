import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n = int(input_())
    if not n:
        print(0)
        continue
    res = ''
    j = 100
    while j:
        j -= 1
        if n > (3 ** j - 1) // 2:
            res += '1'
            n -= 3 ** j
        elif n < -(3 ** j - 1) // 2:
            res += '-'
            n += 3 ** j
        elif res:
            res += '0'
    print(res)
