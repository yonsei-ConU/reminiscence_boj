import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
p = input_().split()
pp = []
for v in p:
    a, b = map(int, v.split('.'))
    pp.append(a * 100 + b)

ans = sum(pp)
buckets = [[], [], [], [], []]
for v in pp:
    buckets[v % 5].append(v)

ans -= len(buckets[1]) + len(buckets[2]) * 2
three = len(buckets[3])
four = len(buckets[4])
while True:
    m = min(three, four)
    three -= m
    four -= m
    ans -= 2 * m
    if four <= 1:
        break
    if not three:
        three += 1
        four -= 2

ans = str(ans - (three >> 1))
ans = '0' * 10 + ans
print(str(int(ans[:-2])) + '.' + ans[-2:])
