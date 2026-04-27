import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


l = [[1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [4, 7], [4, 8], [5, 7], [5, 8], [6, 7], [6, 8], [7, 8]]
while True:
    board = input_().rstrip()
    if board == 'end':
        break
    o = []
    x = []
    if board[0] == board[3] == board[6]:
        if board[0] == 'O':
            o.append(1)
        elif board[0] == 'X':
            x.append(1)
    if board[1] == board[4] == board[7]:
        if board[1] == 'O':
            o.append(2)
        elif board[1] == 'X':
            x.append(2)
    if board[2] == board[5] == board[8]:
        if board[2] == 'O':
            o.append(3)
        elif board[2] == 'X':
            x.append(3)
    if board[0] == board[1] == board[2]:
        if board[0] == 'O':
            o.append(4)
        elif board[0] == 'X':
            x.append(4)
    if board[3] == board[4] == board[5]:
        if board[3] == 'O':
            o.append(5)
        elif board[3] == 'X':
            x.append(5)
    if board[6] == board[7] == board[8]:
        if board[6] == 'O':
            o.append(6)
        elif board[6] == 'X':
            x.append(6)
    if board[0] == board[4] == board[8]:
        if board[0] == 'O':
            o.append(7)
        elif board[0] == 'X':
            x.append(7)
    if board[2] == board[4] == board[6]:
        if board[2] == 'O':
            o.append(8)
        elif board[2] == 'X':
            x.append(8)

    diff = board.count('X') - board.count('O')

    if o and x:
        # print('both win')
        print('invalid')
    elif not o and not x and '.' in board:
        # print('not terminal board')
        print('invalid')
    elif (o and diff) or (x and diff != 1):
        # print('OX count')
        print('invalid')
    elif (len(o) > 1 and o not in l) or (len(x) > 1 and x not in l):
        # print('one side win twice')
        # print(o)
        # print(x)
        print('invalid')
    elif not (0 <= diff <= 1):
        print('invalid')
    else:
        print('valid')
