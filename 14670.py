import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
drugs = [-1] * 101
for i in range(N):
    e, n = minput()
    drugs[e] = n

for _ in range(int(input_())):
    L, *S = minput()
    ans = []
    check = True
    for s in S:
        if drugs[s] == -1:
            check = False
            break
        else:
            ans.append(drugs[s])
    if not check:
        print('YOU DIED')
    else:
        print(*ans)
