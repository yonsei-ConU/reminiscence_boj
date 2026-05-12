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
result = two_sat(N, clauses, True)
if not result:
    output.append('0')
else:
    output.append('1')
    output.append(' '.join(map(lambda x: str(+x), result)))
os.write(1, '\n'.join(output).encode())
os._exit(0)
