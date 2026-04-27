nine = [1]
for i in range(9):nine.append(nine[-1]*9)

n = input()
z = int(n)
n = list(n)
n = list(map(int, n))[::-1]
ans = 0
for i in range(len(n)):
    t = n[i]
    if t > 4:
        t -= 1
    ans += nine[i] * t
print(ans)
