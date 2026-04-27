colors = [input().split() for _ in range(10)]
ans = 0
for i in range(10):
    l = len(set(colors[i]))
    if l == 1:
        ans = 1

for i in range(10):
    l = len(set([colors[j][i] for j in range(10)]))
    if l == 1:
        ans = 1

print(ans)
