import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
a = list(minput())
m = int(input_())

if not n:
    print(a[0] % m)
elif n == 1:
    print(pow(a[1], a[0], m))
else:
    if a[2] == 1:
        print(1)
    else:
        print(pow(a[2], pow(a[1], a[0], m - 1) + m - 1, m))
