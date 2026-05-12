import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for line in sys.stdin:
    line = list(line)
    for i in range(len(line)):
        if line[i] == 'E':
            line[i] = 'I'
        elif line[i] == 'I':
            line[i] = 'E'
        elif line[i] == 'e':
            line[i] = 'i'
        elif line[i] == 'i':
            line[i] = 'e'
    print(''.join(line), end='')
