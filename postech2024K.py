import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

Q = int(input_())
l = []
ps = []

for _ in range(Q):
    query = list(minput())
    if query[0] == 1:
        if not l:
            l.append(query[1])
            ps.append(query[1])
        else:
            l.append(query[1])
            ps.append(query[1] + ps[-1])
    else:
        div = len(l) // 2 - 1
        front = ps[div]
        back = ps[-1] - front
        if front <= back:
            l = l[div+1:]
            new_ps = []
            for i in ps[div+1:]:
                new_ps.append(i - ps[div])
            ps = new_ps[:]
            print(front)
        else:
            l = l[:div+1]
            ps = ps[:div+1]
            print(back)
print(*l)
