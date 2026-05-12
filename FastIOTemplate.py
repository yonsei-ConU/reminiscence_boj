import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
input_ = reader.readline
def minput(): return map(int, input_().split())


output = []
# your code here

os.write(1, '\n'.join(output).encode())
os._exit(0)
