import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n = int(input_())
    s = ['+', '-', '*', '//']
    flag = False
    for i in s:
        for j in s:
            for k in s:
                expression = f'4 {i} 4 {j} 4 {k} 4'
                if eval(expression) == n:
                    print(f'{expression.replace("//", "/")} = {n}')
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    else:
        print('no solution')
# 1:54:12