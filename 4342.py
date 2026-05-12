import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    a, b = minput()
    if a == b == 0:
        break
    if a < b:
        a, b = b, a
    t1 = a // b
    a %= b
    if not a:
        ans = 1
    else:
        ans = t1 != 1
    print(f"{'BA'[ans]} wins")
