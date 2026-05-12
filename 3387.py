import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


K = int(input_())
r = 0 
ok = False

for m in range(1, 1001):
    r = (r * 10 + 1) % K
    for d in range(1, 10):
        if (d * r) % K == 0:
            print(d, m)
            ok = True
            break
    if ok:
        break

if not ok:
    print("Impossible")
