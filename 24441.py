import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


lucky = list(range(1, 1000001, 2))
cur = 1
while True:
    for num in lucky:
        if num > cur:
            break
    else:
        break
    new_lucky = []
    for i in range(len(lucky)):
        if (i + 1) % num:
            new_lucky.append(lucky[i])
    lucky, new_lucky = new_lucky, lucky
    cur = num

print(lucky)
