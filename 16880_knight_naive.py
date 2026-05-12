knight = [[0] * 3000 for _ in range(3000)]
for i in range(481):
    for j in range(481):
        if not i or not j or (i == 1 and j == 1): continue
        next_state = {knight[i - 1][j - 2] if j != 1 else 100000, knight[i - 2][j - 1] if i != 1 else 100000}
        mex = 0
        while mex in next_state:
            mex += 1
        knight[i][j] = mex

for i in range(481):
    for j in range(481):
        print(f"{knight[i][j]: >2}", end='')
    print()
print()
