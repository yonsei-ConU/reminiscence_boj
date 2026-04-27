m = int(input())
n = int(input())
ans = (m + 1) * (n - 1)

for x in range(1, m + 1):
    for y in range(x, m + 1):
        for z in range(y, m + 1):
            if x ** 2 + y ** 2 == z ** 2:
                ans += 1

print(ans)
