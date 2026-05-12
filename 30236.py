import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n = int(input_())
    a = list(minput())
    cur = 1
    for i in range(n):
        if a[i] == cur:
            cur += 1
        cur += 1
    print(cur - 1)
