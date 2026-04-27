import random

secret = random.randint(1, 10**18 - 1)
print(secret)
while True:
    a = int(input())
    if a == secret:
        print('GG')
        exit()
    ret = sum(map(int, list(str(secret + a))))
    print(ret)
    
