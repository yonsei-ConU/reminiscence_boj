import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, x = minput()
t = x - (1 << (n - 1))
if t < 0:
    exit(print('impossible'))
ans = [1] * n
ans[0] += t
output = []
while len(ans) > 1:
    output.append(' '.join(map(str, ans)))
    new_ans = []
    for i in range(len(ans) - 1):
        new_ans.append(ans[i] + ans[i + 1])
    ans, new_ans = new_ans, ans

print(x)
print('\n'.join(output[::-1]))
