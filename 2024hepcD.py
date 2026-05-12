import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_())
if not N:
    print(0)
    exit()
babyak = [[] for _ in range(100)]
for i in range(N):
    l = input_().split()
    w, d, p = map(int, l[1:])
    babyak[7 * w + d].append((l[0], p))
money = dict()
for i in range(N):
    name, m = input_().split()
    money[name] = int(m)

ans = 0
cur = 0
for i in range(100):
    if not babyak[i]:
        cur = 0
    else:
        for b in babyak[i]:
            sunbae, price = b
            if money[sunbae] >= price:
                cur += 1
                break
        else:
            cur = 0
    ans = max(ans, cur)

print(ans)
