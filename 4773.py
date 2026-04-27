import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def parse_roman(numeral):
    try:
        res = 0
        l = len(numeral)
        ptr = 0
        while numeral[ptr] == 'M':
            res += 1000
            ptr += 1
        if numeral[ptr] == 'D':
            res += 500
            ptr += 1
        while numeral[ptr] == 'C':
            res += 100
            ptr += 1
        if numeral[ptr] == 'M':
            res += 800
            ptr += 1
        elif numeral[ptr] == 'D':
            res += 300
            ptr += 1
        while numeral[ptr] == 'C':
            res += 100
            ptr += 1
        if numeral[ptr] == 'L':
            res += 50
            ptr += 1
        while numeral[ptr] == 'X':
            res += 10
            ptr += 1
        if numeral[ptr] == 'C':
            res += 80
            ptr += 1
        elif numeral[ptr] == 'L':
            res += 30
            ptr += 1
        while numeral[ptr] == 'X':
            res += 10
            ptr += 1
        if numeral[ptr] == 'V':
            res += 5
            ptr += 1
        while numeral[ptr] == 'I':
            res += 1
            ptr += 1
        if numeral[ptr] == 'X':
            res += 8
            ptr += 1
        elif numeral[ptr] == 'V':
            res += 3
            ptr += 1
        while numeral[ptr] == 'I':
            res += 1
            ptr += 1
        return res
    except IndexError:
        return res


stack = []
for expression in sys.stdin:
    expression = expression.rstrip()
    if not expression:
        break
    if expression in '+-*/':
        if len(stack) < 2:
            print('stack underflow')
        else:
            first = stack.pop()
            second = stack.pop()
            if expression == '+':
                t = second + first
                stack.append(t)
            elif expression == '-':
                t = second - first
                stack.append(t)
            elif expression == '*':
                t = second * first
                stack.append(t)
            elif expression == '/':
                if not first:
                    print('division by zero exception')
                    stack.append(second)
                else:
                    t = second // first
                    stack.append(t)
    elif expression == '=':
        if not stack:
            print('stack underflow')
        else:
            n = stack[-1]
            if n < 1 or n >= 5000:
                print('out of range exception')
                continue
            res = 'M' * (n // 1000)
            n %= 1000
            if n >= 900:
                n -= 900
                res += 'CM'
            elif n >= 500:
                n -= 500
                res += 'D'
            elif n >= 400:
                n -= 400
                res += 'CD'
            res += 'C' * (n // 100)
            n %= 100
            if n >= 90:
                n -= 90
                res += 'XC'
            elif n >= 50:
                n -= 50
                res += 'L'
            elif n >= 40:
                n -= 40
                res += 'XL'
            res += 'X' * (n // 10)
            n %= 10
            res += ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'][n]
            print(res)
    else:
        stack.append(parse_roman(expression))
