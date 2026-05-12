import io, os
from decimal import Decimal
from math import ceil
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
X = Decimal(sinput())
p = ceil(((8 * X + 1).sqrt() - 1) / 2)
m = (p * (p - 1)) // 2 + 1
n = X - m + 1
o = p - n + 1
if not p & 1:
    output.append(f'{n}/{o}')
else:
    output.append(f'{o}/{n}')
os.write(1, '\n'.join(output).encode())
os._exit(0)
