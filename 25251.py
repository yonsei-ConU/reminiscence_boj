import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


h, w = minput()
house = [input_().rstrip() for _ in range(h)]
left = w
right = 0
ans = 0
for row in house[::-1]:
    C = [i for i in range(w) if row[i] == 'C']
    if not C:
        continue
    elif len(C) == 1:
        cur_left = cur_right = C[0]
    else:
        cur_left = C[0]
        cur_right = C[-1]
    if cur_right > left:
        ans += 1
    left = cur_left
    right = cur_right

print(ans)
