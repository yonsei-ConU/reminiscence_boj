import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
K = int(input_())
par = [0] * 101
while 1:
    lst = list(minput())
    if lst[0] == -1:
        break
    for i in range(1, len(lst)):
        par[lst[i]] = lst[0]
while 1:
    output.append(str(K))
    K = par[K]
    if not K:
        break

os.write(1, ' '.join(output).encode())
os._exit(0)
