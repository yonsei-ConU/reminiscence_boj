import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    l = sorted(list(minput()))
    if not sum(l):
        break
    if l[0] == l[1] == l[2]:
        if l[0] == 13:
            print('*')
        else:
            x = l[0] + 1
            print(x, x, x)
    elif l[0] == l[1]:
        if l[0] == 13:
            if l[2] == 12:
                print('1 1 1')
            else:
                print(l[0], l[1], l[2] + 1)
        else:
            if l[2] == 13:
                print(1, l[0] + 1, l[0] + 1)
            else:
                print(l[0], l[0], l[2] + 1)
    elif l[1] == l[2]:
        if l[0] == 12:
            print('1 1 1')
        elif l[0] + 1 == l[1]:
            print(l[1], l[2], l[0] + 2)
        else:
            print(l[0] + 1, l[1], l[2])
    else:
        print('1 1 2')
