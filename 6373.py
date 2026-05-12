import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for num_str in sys.stdin:
    num_str = num_str.rstrip()
    if not num_str:
        break
    digit_count = len(num_str)
    ans = True
    for i in range(2, digit_count + 1):
        tmp = f'{int(num_str) * i:0>{digit_count}}'
        ans = ans and tmp in num_str * 2
    n0t = ' not' * (1 - ans)
    print(f'{num_str} is{n0t} cyclic')
