import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='ascii')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
N = int(input_())
A = [sinput().rstrip() for _ in range(N)]
bits = [0] * 1024
for i in range(N):
    element = A[i]
    mask = 0
    for char in element:
        mask |= 1 << int(char)
    bits[mask] += 1

ans = 0
for b in bits:
    if b >= 2:
        ans += b * (b - 1) >> 1

for i in range(1024):
    for j in range(i + 1, 1024):
        if i & j:
            ans += bits[i] * bits[j]

output.append(str(ans))

os.write(1, '\n'.join(output).encode())
os._exit(0)
