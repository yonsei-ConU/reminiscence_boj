import io, os, sys
from algorithms import two_sat
sys.setrecursionlimit(12345)
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
N, M = minput()
clauses = [list(minput()) for _ in range(M)]
output.append(str(two_sat(N, clauses)))
os.write(1, '\n'.join(output).encode())
os._exit(0)
