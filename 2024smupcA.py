import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

l = input().split()
N = int(l[0])
S = l[1]
alphabets = set()
ans = ''
wasted = 0
for s in S:
    if s not in alphabets:
        ans += s
        alphabets.add(s)
    else:wasted += 1
ans += str(wasted + 4)
ans = str(N + 1906) + ans
ans = ans[::-1]
print('smupc_' + ans)
