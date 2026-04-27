from random import *

def f():
    ret = ''
    l = randint(3, 15)
    for i in range(l):
        ret += choice(['H', 'T'])
    return l, ret

def g(x):
    print(x)
    for i in range(x):
        _, a = f()
        print(a)
print(g(10))
