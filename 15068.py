import sys
input_= sys.stdin.readline
def minput(): return map(int, input_().split())


conversion = input().split()
n, conversion = int(conversion[0]), conversion[1:]
x = 1
d = []
d.append(conversion.pop())
l = [1]
not_one = []

for i in range(n - 2, -1, -1):
    mult = int(conversion.pop())
    x *= mult
    d.append(conversion.pop())
    l.append(x)
    if mult != 1:
        not_one.append(i)

k = int(input())
result = []
l = l[::-1]
d = d[::-1]
print(not_one)
for i in range(n):
    amount = k // l[i]
    result.append(amount * l[i])
    k -= amount * l[i]
print(result)
ps_reverse = []
t = 0
for i in range(n-1, -1, -1):
    t += result[i]
    ps_reverse.append(t)

ps_reverse.reverse()
print(result[0] // l[0] + (ps_reverse[1] * 2 >= l[0]), d[0])
if n == 2:
    print(result[0] // l[0], d[0], result[1], d[1])
else:
    print(result[0] // l[0], d[0], result[1] // l[1] + (ps_reverse[2] * 2 >= l[1]), d[1])
