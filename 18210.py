import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


t = int(input_())
if t <= 3: exit(print(t))
ans = 1
cur_sum = 1
x = 3
while True:
    cur_sum += x << 1
    if cur_sum > t:
        if cur_sum - x > t:
            cur_sum -= x << 1
        else:
            cur_sum -= x
            ans += 1
        break
    elif cur_sum == t:
        break
    ans += 2
    x *= 3

t -= cur_sum
assert t >= 0
while t:
    ans += t % 3
    t //= 3

print(ans)
