import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    m, k = minput()
    p = list(minput())
    mx = max(p)
    lo = mx - 1
    hi = 50000000001
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        mTE = 1
        cur_sum = 0
        for v in p:
            cur_sum += v
            if cur_sum > mid:
                cur_sum = v
                mTE += 1
        if mTE <= k:
            hi = mid
        else:
            lo = mid
    ans = []
    cur_sum = 0
    temp = 0
    for i in range(m - 1, -1, -1):
        if cur_sum + p[i] > hi or i + 2 == k - len(ans):
            ans.append(temp)
            temp = 1
            cur_sum = p[i]
        else:
            cur_sum += p[i]
            temp += 1
    ans.append(temp)
    ans = ans[::-1]
    output = []
    ptr = 0
    for value in ans:
        for i in range(value):
            output.append(str(p[ptr]))
            ptr += 1
        output.append('/')
    output.pop()
    print(' '.join(output))
