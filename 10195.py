import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


tc = int(input_())
for i in range(1, tc + 1):
    l = input_().split()
    depth = length = -1
    for element in l:
        if element.isdigit():
            if depth == -1: depth = int(element)
            else: length = int(element)
    stalagmites = [-1] * length
    for _ in range(int(input_().split()[0])):
        s = input_().split()
        d = l = -1
        for element in s:
            if element.isdigit():
                if d == -1: d = int(element)
                else: l = int(element)
        stalagmites[l] = d
    print(f"Case: {i}")
    for _ in range(int(input_().split()[0])):
        seq = input_().strip()
        x = 0
        y = depth - 1
        result = 'Reached end of tunnel'
        for move in seq:
            if move == 'v':
                y -= 1
            elif move == '^':
                y += 1
            x += 1
            if y == -1:
                result = 'Crashed into tunnel floor'
                break
            elif stalagmites[x] > y:
                result = 'Crashed into stalagmite'
                break
            elif y == depth:
                result = 'Crashed into tunnel ceiling'
                break
        print(f"Sequence {seq} {result}")
    if i != tc:
        input_()
