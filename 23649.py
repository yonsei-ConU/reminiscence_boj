import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


seq = list(input_().rstrip())
rev = 0
adjust = [{'l': 'l', 'r': 'r'}, {'l': 'r', 'r': 'l'}]

ans = []
streak = 0
last = ''
while seq:
    cur = seq.pop()
    if cur == last:
        streak += 1
    else:
        if last == 'b':
            ans.append(last * (streak % 2))
        else:
            ans.append(last * (6 - streak % 6))
        streak = 1
        last = cur

if streak:
    if last == 'b':
        ans.append(last * (streak % 2))
    else:
        ans.append(last * (6 - streak % 6))

print(''.join(ans))
