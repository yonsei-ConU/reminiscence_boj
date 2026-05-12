import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, B = minput()
properties = list(minput())
left = 0
right = 0
ans = 0
cur_sum = properties[0]

while right < N:
    if cur_sum <= B:
        ans = max(ans, right - left + 1)
        right += 1
        if right < N:
            cur_sum += properties[right]
    else:
        cur_sum -= properties[left]
        left += 1
        if left > right:
            right = left
            if right < N:
                cur_sum = properties[right]

print(ans)
