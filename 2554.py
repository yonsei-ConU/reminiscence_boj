def f(x):
    if x < 10:
        return [1,1,2,6,4,2,2,4,2,8][x]
    s = str(x)
    if int(s[-2]) % 2:
        return 4 * f(x//5) * f(int(s[-1]))
    else:
        return 6 * f(x//5) * f(int(s[-1]))

def g(s):
    fac = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]
    eig = [6, 8, 4, 2]
    s = str(s)
    n = len(s)

    if n == 1:
        tmp = int(s[0])
        return fac[tmp]

    if n == 2:
        tmp1 = int(s[0])
        tmp2 = int(s[1])
        tmp1 %= 4
        return (eig[tmp1] * fac[tmp2]) % 10

    k = int(s[-1])
    x1 = int(s[-3])
    x2 = int(s[-2])
    x = x1 * 10 + x2
    q = x % 4

    return (eig[q] * fac[k]) % 10



wa = 0
for i in range(1, 100000000):
    try:
        if f(i) % 10 != g(i):
            wa += 1
    except KeyboardInterrupt:
        print(i)
        print(wa)
        break

print(wa)
