import io, os
from math import lcm
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
N = int(input_())
A = list(map(lambda x: 2 * int(x), input_().split()))
output.append(str(lcm(*A)))
os.write(1, '\n'.join(output).encode())
os._exit(0)
