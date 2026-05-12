import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
MOD = 10 ** 9 + 7
N = int(input_())
h = list(minput())
ans = 1
last_idx = 0
cur_h_max = h[0]
for i in range(1, N):
    if h[i] > cur_h_max:
        ans = (ans * (i - last_idx + 1)) % MOD
        cur_h_max = h[i]
        last_idx = i
output.append(str(ans))
os.write(1, '\n'.join(output).encode())
os._exit(0)
