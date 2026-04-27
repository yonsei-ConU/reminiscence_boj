import sys
from fractions import Fraction
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    data = input_().rstrip()
    if direction == '#':
        break
    direction = []
    while data:
        if data.startswith("north"):
            direction.append(0)
            data = data[5:]
        else:
            assert data.startswith("west")
            direction.append(1)
            data = data[4:]
        
