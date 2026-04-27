import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, m = minput()
if not n % 2 and not m % 2:
    print(n * m)
    x = 1
    y = 2
    while y != m:
        print(x, y)
        if not y % 2:
            while x != n // 2:
                x += 1
                print(x, y)
        else:
            while x != 1:
                x -= 1
                print(x, y)
        y += 1
    for x in range(1, n + 1):
        print(x, y)
    y -= 1
    while y != 1:
        print(x, y)
        if not y % 2:
            while x != n:
                x += 1
                print(x, y)
        else:
            while x != n // 2 + 1:
                x -= 1
                print(x, y)
        y -= 1
    for x in range(n, 0, -1):
        print(x, y)

elif n % 2 and not m % 2:
    print(n * m)
    x = 1
    y = 2
    while y != m:
        print(x, y)
        if not y % 2:
            while x != n - 1:
                x += 1
                print(x, y)
        else:
            while x != 1:
                x -= 1
                print(x, y)
        y += 1
    for x in range(1, n + 1):
        print(x, y)
    while y != 1:
        y -= 1
        print(x, y)
    for x in range(n - 1, 0, -1):
        print(x, y)

elif not n % 2 and m % 2:
    print(n * m)
    x = 2
    y = 1
    while x != n:
        print(x, y)
        if not x % 2:
            while y != m - 1:
                y += 1
                print(x, y)
        else:
            while y != 1:
                y -= 1
                print(x, y)
        x += 1
    for y in range(1, m + 1):
        print(x, y)
    while x != 1:
        x -= 1
        print(x, y)
    for y in range(m - 1, 0, -1):
        print(x, y)

elif m == n == 3:
    print("""8
1 1
2 1
3 1
3 2
3 3
2 3
1 3
1 2""")

else:
    print(n * m - 1)
    x = 1
    y = 2
    while y != m - 1:
        print(x, y)
        if not y % 2:
            while x != n - 1:
                x += 1
                print(x, y)
        else:
            while x != 1:
                x -= 1
                print(x, y)
        y += 1
    print(1, m - 1)
    print(1, m)
    print(2, m)
    print(3, m)
    x = 3
    while x != n:
        print(x, m - 1)
        print(x + 1, m - 1)
        print(x + 1, m)
        print(x + 2, m)
        x += 2
    for y in range(m - 1, 0, -1):
        print(x, y)
    for x in range(n - 1, 0, -1):
        print(x, y)
