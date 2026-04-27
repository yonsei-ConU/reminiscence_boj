N = int(input())
encrypted = input().split()
for element in encrypted:
    if int(element[0]) < 3:
        print('.', end='')
    else:
        print('-', end='')
