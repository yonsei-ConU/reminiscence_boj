from decimal import *
getcontext().prec = 120
factorial_inv = [Decimal(1)] * 2
tmp = Decimal(1)
pi = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")


for i in range(2, 51):
    tmp /= Decimal(i)
    factorial_inv.append(tmp)


def twopi_mod(x):
    while x < -pi:
        x += 2*pi
    while x > 2*pi:
        x -= 2*pi
    return x
  

def sin(x):
    x = twopi_mod(x)
    r = Decimal(0)
    sgn_tmp = Decimal(1)
    for power in range(1, 51, 2):
        r += sgn_tmp * (x ** Decimal(power)) * factorial_inv[power]
        sgn_tmp *= -1
    return r


def cos(x):
    x = twopi_mod(x)
    r = Decimal(1)
    sgn_tmp = Decimal(-1)
    for power in range(2, 52, 2):
        r += sgn_tmp * (x ** Decimal(power)) * factorial_inv[power]
        sgn_tmp *= -1
    return r


a, b, c = map(Decimal, input().split())

x = c / a

while abs(a*x + b*sin(x) - c) > Decimal("0.0000000000000000000000000000000000000000000000000000000001"):
    x -= (a*x + b*sin(x) - c) / (a + b*cos(x))

print(round(x, 6))
