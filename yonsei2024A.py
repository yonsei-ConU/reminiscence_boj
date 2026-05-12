import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
N = int(input_())
if N % 2024 or N > 100000:
    output.append('No')
else:
    output.append('Yes')
os.write(1, '\n'.join(output).encode())
os._exit(0)
