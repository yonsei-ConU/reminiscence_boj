import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
n, m = minput()
if m < n - 1: assert False
output.append(['Alice', 'Bob'][(m - n + 1) & 1])
os.write(1, '\n'.join(output).encode())
os._exit(0)
