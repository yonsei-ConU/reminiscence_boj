import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    input_()
    s = sorted(list(input_().rstrip()))
    a = int(s[0])
    b = int(''.join(s[1:][::-1]))
    print(a + b)
