import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, x, y = minput()
r = list(minput())
b = list(minput())
S = sum(r) + sum(b)
A = [(r[i], b[i], i) for i in range(n)]
A.sort(key=lambda x: -x[0] / x[1])
threshold = x / y / 2
ans = [''] * n
cur_qx = 0
for p, q, i in A:
    if cur_qx + q / S <= threshold:
        cur_qx += q / S
        ans[i] = '1'
    elif cur_qx < threshold:
        remain = threshold - cur_qx
        cur_qx = threshold
        if remain > 1: remain = 1
        elif remain < 0: remain = 0
        ans[i] = str(remain)
    else:
        ans[i] = '0'

sys.stdout.write('\n'.join(ans))
