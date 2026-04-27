import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
S = input_().rstrip()
p = [i for i in range(N) if S[i] == 'P']
c = [i for i in range(N) if S[i] == 'C']
m = min(len(p), len(c))
p = p[:m]
c = c[:m]
ans = []
for i in range(N):
    if i in p:
        ans.append('C')
    elif i in c:
        ans.append('P')
    else:
        ans.append(S[i])

print(''.join(ans))
