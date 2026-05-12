import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n = int(input_())
    a = list(minput())
    a_rev = [0] * 1001
    for i in range(n):
        a_rev[a[i]] = i
    if abs(a_rev[1] - 500) <= 50:
        print("Bob")
    else:
        print("Alice")
