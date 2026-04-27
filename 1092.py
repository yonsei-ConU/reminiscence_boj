import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
cranes = sorted(tuple(minput()), reverse=True)
M = int(input_())
box = sorted(tuple(minput()), reverse=True)
if box[0] > cranes[0]:
    exit(print(-1))
ans = 0

while box:
    ans += 1
    for crane in cranes:
        for b in box:
            if crane >= b:
                box.remove(b)
                break

print(ans)
    
