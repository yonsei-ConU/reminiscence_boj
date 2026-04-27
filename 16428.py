a, b = map(int, input().split())
x, y = a//b, a%b
if y < 0:
    y += abs(b)
    x -= int(abs(b) / b)
print(x)
print(y)
