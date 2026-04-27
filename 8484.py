import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
c = list(minput())

for _ in range(int(input_())):
    a, b = minput()
    a -= 1; b -= 1
    if b - a < 2:
        print('NIE')
    elif b - a > 44:
        print('TAK')
    else:
        chk = False
        for i in range(a, b + 1):
            for j in range(i + 1, b + 1):
                for k in range(j + 1, b + 1):
                    s = c[i] + c[j] + c[k]
                    m = max(c[i], c[j], c[k])
                    if s - m > m:
                        chk = True
                        break
                if chk:
                    break
            if chk:
                break
        print("NTIAEK"[chk::2])
