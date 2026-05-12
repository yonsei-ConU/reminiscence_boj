import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())
def makelist(x): return [str(x//1000), str((x%1000)//100), str((x%100)//10), str(x%10)]


output = []
N = int(input_())
secret = makelist(N)
for _ in range(int(input_())):
    guess = makelist(int(input_()))
    A = sum(1 for i in range(4) if guess[i] in secret)
    B = sum(1 for i in range(4) if secret[i] == guess[i])
    output.append(f"{A} {B}")
os.write(1, '\n'.join(output).encode())
os._exit(0)
